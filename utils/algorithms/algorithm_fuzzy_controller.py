import os
import random
from typing import List, Tuple
import json

import pygame

from utils.car import Car


class AlgorithmFuzzyController:
    def __init__(self, width: int = 1280, height: int = 720):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.x = 15
        self.index = 0
        self.result = "game not decided"
        self.exit = False
        self.freeze = False
        self.end = False
        self.path_data = []

    def play(self, save_frames: bool, freeze_on_end: bool, save_logs: bool) -> None:
        self.freeze = freeze_on_end
        car_image = self.__load_car_image()
        car = self.__create_car()
        turning_state = True
        approaching_state = False
        braking_state = False

        while not self.exit:
            self.__button_force_exit_handle()
            dt = self.clock.get_time() / 1000

            if not self.end:

                # RULE #1
                if turning_state:
                    car, state = self.__turning_rule(car)
                    if state:
                        turning_state = False
                        approaching_state = True

                # RULE #2
                if approaching_state:
                    car, state, direction = self.__approaching_rule(car)
                    if state:
                        approaching_state = False
                        braking_state = True

                # RULE #3
                if braking_state:
                    car, state = self.__braking_rule(car, direction)
                    if state:
                        braking_state = False
                        car.steering = 0

                car.steering = max(
                    -car.max_steering, min(car.steering, car.max_steering)
                )
                car.update(dt)

                self.screen.fill((0, 0, 0))
                pygame.draw.rect(
                    self.screen, (255, 0, 0), pygame.Rect(400, 0, 460, 120), 2
                )
                rotated = pygame.transform.rotate(car_image, car.angle)
                rect = rotated.get_rect()

                cur_car_position = car.position * 32 - (rect.width / 2, rect.height / 2)

                self.__check_lose_condition(car, cur_car_position)
                self.__check_winning_condition(car)

                self.screen.blit(rotated, cur_car_position)
                pygame.display.flip()
                if save_frames:
                    pygame.image.save(self.screen, f"plots/frame{self.index}.jpg")
                    self.index += 1
                self.clock.tick(self.ticks)
                self.path_data.append([car.position.x, car.position.y, car.angle])
        if save_logs:
            f = open("code/lab08/path_log.txt","w+")
            f.write(self.__parse_to_json(self.path_data))
            f.close()
        pygame.quit()

    def get_game_result(self) -> str:
        return self.result

    def __check_lose_condition(self, car: Car, cur_car_position: List[float]) -> None:
        if (
            cur_car_position[0] < -8
            or cur_car_position[1] < -6
            or cur_car_position[1] > 640
            or cur_car_position[0] > 1150
        ):
            car.stop()
            self.result = "failed"
            if self.freeze == False:
                self.exit = True
            self.end = True

    def __check_winning_condition(self, car: Car) -> None:
        if car.angle > 0 and car.angle < 20 or car.angle > 160 and car.angle < 180:
            if (
                car.position.x > 14
                and car.position.x < 26
                and car.position.y > 0
                and car.position.y < 3
            ):
                car.stop()
                self.result = "succeed"
                if self.freeze == False:
                    self.exit = True
                self.end = True

    def __braking_rule(self, car: Car, direction: bool) -> Tuple[Car, bool]:
        state = False
        if direction:
            car.steering = 50
        else:
            car.steering = -50
        if car.angle > -5 and car.angle < 5:
            state = True
        return car, state

    def __approaching_rule(self, car: Car) -> Tuple[Car, bool, bool]:
        state = False
        if car.position.x > 20:
            car.steering = 5
            direction = True
        if car.position.x < 20:
            car.steering = -5
            direction = False
        if car.position.y < 8.5:
            state = True
        return car, state, direction

    def __turning_rule(self, car: Car) -> Tuple[Car, bool]:
        state = False
        if car.angle >= 0 and car.angle < 90:
            car.steering = 50
        if car.angle >= 90 and car.angle < 180:
            car.steering = -50
        if car.angle >= 180 and car.angle < 270:
            car.steering = -50
        if car.angle >= 270 and car.angle < 360:
            car.steering = 50
        if car.angle > 88 and car.angle < 92:
            car.steering = 0
            state = True
        return car, state

    def __button_force_exit_handle(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def __create_car(self) -> Car:
        start_x = random.randint(5, 20)
        start_y = random.randint(7, 20)
        deg = random.randint(5, 360)
        return Car(start_x, start_y, deg)

    def __load_car_image(self) -> object:
        current_dir = os.path.dirname(os.path.abspath("ssi"))
        image_path = os.path.join(current_dir, "assets/car.png")
        return pygame.image.load(image_path)

    def __parse_to_json(self, data: List) -> str:
        return json.dumps(data)
