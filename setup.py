from setuptools import setup

package_name = 'dance_move_detector'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='ROS2 Virtual Dance Move Detector Simulation',
    license='MIT',
    entry_points={
        'console_scripts': [
            'dance_publisher = dance_move_detector.dance_publisher:main',
            'dance_subscriber = dance_move_detector.dance_subscriber:main',
        ],
    },
)
