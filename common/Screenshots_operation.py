import os
import time

File_Name = str(time.strftime("%Y%m%d%H%M%S")) + ".png"
path_phone = "storage/emulated/0/DCIM/Screenshots/" + File_Name
path_pc = 'C:\\Users\\syf\\PycharmProjects\\flashsign_HR\\TestScreenshots'


class Screenshots:

    def crop_image(self, path_jt):
        """截图到手机"""
        os.system('adb shell screencap -p {}'.format(path_jt))
    def remove_image(self):
        os.system('adb shell rm {}'.format(path_phone))

    def move_image(self, path_yd, path_jt):
        """
        移动图片到电脑
        :param path_yd: 移动电脑路径
        :param path_jt:手机截图生成的路径
        :return:
        """
        os.system('adb pull {} {}'.format(path_jt, path_yd))

    def execute_screenshot(self):
        self.crop_image(path_jt=path_phone)
        print("{}截图已保存到手机".format(File_Name))
        self.move_image(path_jt=path_phone, path_yd=path_pc)
        print("截图已移动到pc目录{}".format(path_pc))
        self.remove_image()
        print("手机图片{}已删除".format(File_Name))


    def path_lj(self):
        """
        :return: 返回图片路径，在电脑上的
        """
        path_image = path_pc + "\\" + File_Name
        return path_image

    def flie_jt(self):
        with open(Screenshots().path_lj(), mode="rb") as f:
            file = f.read()
        return file
