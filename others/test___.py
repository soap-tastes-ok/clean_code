#%%
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field


@dataclass(frozen=False, init=False)
class AbstractDataClass(ABC):
    # IMAGE_PATH: str
    # HEIGHT_IN_PX: int  # 画面縦方向
    # WIDTH_IN_PX: int  # 画面横方向

    @property
    @abstractmethod
    def IMAGE_PATH(self):
        pass

    # @abstractproperty
    # def HEIGHT_IN_PX(self):
    #     raise NotImplementedError

    # @abstractproperty
    # def WIDTH_IN_PX(self):
    #     raise NotImplementedError


class EgoDataClass(AbstractDataClass):
    # IMAGE_PATH = "/images/truck.png"
    HEIGHT_IN_PX = 25  # 画面縦方向
    WIDTH_IN_PX = 150  # 画面横方向


# ego = EgoDataClass()
EgoDataClass


# %%
vars(EgoDataClass)


#%%
# %%

# class Class8TruckDataClass(AbstractDataClass):
#     IMAGE_PATH = "/images/truck.png"
#     HEIGHT_IN_PX = 25  # 画面縦方向
#     # WIDTH_IN_PX = 150  # 画面横方向
#     # # example of 2m truck in
#     # # https://www.ec-life.co.jp/blogs/truck-20210401/
#     # cg_height: float = 1.5
#     # # example in http://www.hyotokyo.or.jp/news/wp-content/
#     # # uploads/2016/12/20161202_questionnaire_03admin.pdf
#     # tire_distance: float = 1.9
#     # # Future work:
#     # # add maximum_wheel_angle for other vehicle type.
#     # # https://www.kenworth.com/about-us/news/wolfe-movers/
#     # maximum_wheel_angle: int = 45
#     # tire_position_dict: dict = {
#     #     0: {
#     #         "left": {
#     #             "position_from_top": 0.1,
#     #             "direction_sign_to_y": 0.9,
#     #         },
#     #         "right": {
#     #             "position_from_top": 0.1,
#     #             "direction_sign_to_y": -0.9,
#     #         },
#     #     },
#     #     1: {
#     #         "left": {
#     #             "position_from_top": 0.4,
#     #             "direction_sign_to_y": 0.9,
#     #         },
#     #         "right": {
#     #             "position_from_top": 0.4,
#     #             "direction_sign_to_y": -0.9,
#     #         },
#     #     },
#     #     2: {
#     #         "left": {
#     #             "position_from_top": 0.5,
#     #             "direction_sign_to_y": 0.9,
#     #         },
#     #         "right": {
#     #             "position_from_top": 0.5,
#     #             "direction_sign_to_y": -0.9,
#     #         },
#     #     },
#     #     3: {
#     #         "left": {
#     #             "position_from_top": 0.8,
#     #             "direction_sign_to_y": 0.9,
#     #         },
#     #         "right": {
#     #             "position_from_top": 0.8,
#     #             "direction_sign_to_y": -0.9,
#     #         },
#     #     },
#     #     4: {
#     #         "left": {
#     #             "position_from_top": 0.9,
#     #             "direction_sign_to_y": 0.9,
#     #         },
#     #         "right": {
#     #             "position_from_top": 0.9,
#     #             "direction_sign_to_y": -0.9,
#     #         },
#     #     },
#     # }
