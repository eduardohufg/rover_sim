from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rover_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
	(os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
	(os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eduardo',
    maintainer_email='eduardochavezmartin10@gmail.com',
    description='Q-mars 2025 simulation',
    license='All reserve Quantum Robotics',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
