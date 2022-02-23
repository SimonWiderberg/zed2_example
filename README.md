# zed2_example

1. Plug in ZED2 camera with USB cable

2. Download latest ZED SDK:
    Website: https://www.stereolabs.com/developers/release/

3. Install ZED python API: 
	website: https://www.stereolabs.com/docs/app-development/python/install/
	pip-install prerequisites: 
    ==
    python -m pip install cython numpy opencv-python pyopengl
    ==
	Open up a terminal as admin and find your SDK install directory.
	Once in the SDK isntall directory type: 
    ==
    python get_python_api.py
    ==

4. Import "pyzed.sl" to your python project 
	some IDEs might complain that the import fails, but if you run the python script inside a terminal it should work

5. run detect_camera.py to check if installation 