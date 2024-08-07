import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'motor_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jevgeni',
    maintainer_email='jevgeni.kalbin@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'twist_to_motor_commands_node = motor_control.twist_to_motor_commands:main',
            'joy_to_twist_node = motor_control.joy_to_twist:main',
            'relay_control_server = motor_control.relay_control_server:main',
            'relay_control_client = motor_control.relay_control_client:main',
            'roboclaw_control_node = motor_control.roboclaw_control:main',
        ],
    },
)
