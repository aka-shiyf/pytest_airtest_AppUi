import os
import time

path_phone = "sdcard/" + str(time.strftime("%Y%m%d%H%M%S")) + ".png"
path_pc = 'E:\调试截图'


class Screenshots:

    def crop_image(self, path_jt):
        """截图到手机"""
        os.system('adb shell screencap -p {}'.format(path_jt))

    def move_image(self, path_yd, path_jt):
        """
        移动图片到电脑
        :param path_yd: 移动电脑路径
        :param path_jt:手机截图生成的路径
        :return:
        """
        os.system('adb pull {} {}'.format(path_jt, path_yd))

    def execute_screenshot(self):
        Screenshots().crop_image(path_jt=path_phone)
        Screenshots().move_image(path_jt=path_phone, path_yd=path_pc)

    def path_lj(self):
        """
        :return: 返回图片路径，在电脑上的
        """
        path_image = path_pc + path_phone
        return path_image

