from PyQt5.QtWidgets import *
from view import Ui_MainWindow
from module_volume import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_ans_cub.clicked.connect(lambda: self.answer_cube())
        self.button_ans_sph.clicked.connect(lambda: self.answer_sphere())
        self.button_ans_cyc.clicked.connect(lambda:self.answer_cylinder())
        self.button_ans_cone.clicked.connect(lambda:self.answer_cone())
        self.button_ans_rcpr.clicked.connect(lambda:self.answer_rcpr())

    def answer_cube(self) -> None:
        """
        Function to set up events when the 'Get Answers' button on Tab Cube is clicked.
        """
        try:
            side = float(self.entry_side.text())
            output = volume_cube(side)

            if self.radio_roundup_cube.isChecked():
                self.label_output.setText(f'The volume of a cube with side of {side} is {output:.2f}')
            else:
                self.label_output.setText(f'The volume of a cube with side of {side} is {output}')
            self.label_output.setStyleSheet("font-weight:bold; color:green")

        except:
            self.label_output.setText('Invalid input, please enter positive numbers!')
            self.label_output.setStyleSheet("color: red")

        finally:
            self.entry_side.clear()
            self.radio_roundup_cube.setChecked(False)

    def answer_sphere(self) -> None:
        """
            Function to set up events when the 'Get Answers' button on Tab Sphere is clicked.
        """
        try:
            radius = float(self.entry_radius.text())

            if self.radio_pi_sphere.isChecked():
                if self.radio_roundup_sphere.isChecked():
                    self.label_output.setText(f'The volume of a sphere with radius of {radius} is {volume_sphere_nopi(radius):.2f}π')
                else:
                    self.label_output.setText(f'The volume of a sphere with radius of {radius} is {volume_sphere_nopi(radius)}π')
            else:
                if self.radio_roundup_sphere.isChecked():
                    self.label_output.setText(f'The volume of a sphere with radius of {radius} is {volume_sphere(radius):.2f}')
                else:
                    self.label_output.setText(f'The volume of a sphere with radius of {radius} is {volume_sphere(radius)}')

            self.label_output.setStyleSheet("font-weight:bold; color:green")

        except:
            self.label_output.setText('Invalid input, please enter positive numbers!')
            self.label_output.setStyleSheet("color: red")

        finally:
            self.entry_radius.clear()
            self.radio_roundup_sphere.setChecked(False)
            self.radio_pi_sphere.setChecked(False)

    def answer_rcpr(self) -> None:
        """
            Function to set up events when the 'Get Answer' button on Tab Rectangular Prism is clicked.
        """
        try:
            height = float(self.entry_height_rcpr.text())
            width = float(self.entry_width_rcpr.text())
            length = float(self.entry_length_rcpr.text())

            output = volume_rcpr(width, length, height)

            if self.radio_roundup_rcpr.isChecked():
                self.label_output.setText(f'The volume of a cube with length={length}, height={height} and width={width} is {output:.2f}')
            else:
                self.label_output.setText(f'The volume of a cube with length={length}, height={height} and width={width} is {output}')
            self.label_output.setStyleSheet("font-weight:bold; color:green")

        except:
            self.label_output.setText('Invalid input, please enter positive numbers!')
            self.label_output.setStyleSheet("color: red")

        finally:
            self.entry_height_rcpr.clear()
            self.entry_width_rcpr.clear()
            self.entry_length_rcpr.clear()
            self.radio_roundup_rcpr.setChecked(False)

    def answer_cone(self) -> None:
        """
            Function to set up events when the 'Get Answer' button on Tab Cone is clicked.
        """
        try:
            radius = float(self.entry_radius_cone.text())
            height = float(self.entry_height_cone.text())

            if self.radio_pi_cone.isChecked():
                output = volume_cone_nopi(radius, height)
                if self.radio_roundup_cone.isChecked():
                    self.label_output.setText(
                        f'The volume of a cone with radius={radius} and height={height} is {output:.2f}π')
                else:
                    self.label_output.setText(
                        f'The volume of a cone with radius={radius} and height={height} is {output}π')
            else:
                output = volume_cone(radius, height)
                if self.radio_roundup_cone.isChecked():
                    self.label_output.setText(
                        f'The volume of a cone with radius={radius} and height={height} is {output:.2f}')
                else:
                    self.label_output.setText(
                        f'The volume of a cone with radius={radius} and height={height} is {output}')
            self.label_output.setStyleSheet("font-weight:bold; color:green")
        except:
            self.label_output.setText('Invalid input, please enter positive numbers!')
            self.label_output.setStyleSheet("color: red")

        finally:
            self.entry_height_cone.clear()
            self.entry_radius_cone.clear()
            self.radio_roundup_cone.setChecked(False)
            self.radio_pi_cone.setChecked(False)

    def answer_cylinder(self) -> None:
        """
            Function to set up events when the 'Get Answer' button on Tab Cylinder is clicked.
        """
        try:
            radius = float(self.entry_radius_cyc.text())
            height = float(self.entry_height_cyc.text())

            if self.radio_pi_cylinder.isChecked():
                output = volume_cylinder_nopi(radius, height)
                if self.radio_roundup_cylinder.isChecked():
                    self.label_output.setText(
                        f'The volume of a cylinder with radius={radius} and height={height} is {output:.2f}π')
                else:
                    self.label_output.setText(
                        f'The volume of a cylinder with radius={radius} and height={height} is {output}π')
            else:
                output = volume_cylinder(radius, height)
                if self.radio_roundup_cylinder.isChecked():
                    self.label_output.setText(f'The volume of a cylinder with radius={radius} and height={height} is {output:.2f}')
                else:
                    self.label_output.setText(f'The volume of a cylinder with radius={radius} and height={height} is {output}')
            self.label_output.setStyleSheet("font-weight:bold; color:green")

        except:
            self.label_output.setText('Invalid input, please enter positive numbers!')
            self.label_output.setStyleSheet("color: red")

        finally:
            self.entry_radius_cyc.clear()
            self.entry_height_cyc.clear()
            self.radio_roundup_cylinder.setChecked(False)
            self.radio_pi_cylinder.setChecked(False)








