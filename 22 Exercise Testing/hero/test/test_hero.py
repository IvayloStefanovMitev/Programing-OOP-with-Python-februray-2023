from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_initialisation(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_if_battle_my_self_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_less_than_one_health_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_with_less_than_one_health_raises_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_hero_and_enemy_with_less_than_1_health_at_same_time(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)

    def test_battle_if_hero_defeat_enemy(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_if_enemy_defeat_hero(self):
        self.hero, self.enemy = self.enemy, self.hero

        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test__str__(self):
        self.assertEqual("Hero Hero: 1 lvl\n"
                         "Health: 100\n"
                         "Damage: 100\n", str(self.hero))


if __name__ == "__main__":
    main()
