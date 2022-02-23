# Zed2 installation

Recommended specifications: https://www.stereolabs.com/docs/installation/specifications/

---

### Installation
1. Plug in ZED2 camera with the USB cable.

2. Download latest ZED SDK:
    https://www.stereolabs.com/developers/release/

    If CUDA is not already installed, the SDK installer will promt you to download and install CUDA

3. Install ZED python API: 
	https://www.stereolabs.com/docs/app-development/python/install/
	
4. pip-install prerequisites: 
    
    ```
        python -m pip install cython numpy opencv-python pyopengl
    ```

5. Open up a terminal as admin and locate your SDK install directory.
	
    Once inside the SDK install directory run:
   
    ```
        python get_python_api.py
    ```

4. To use the API, import "pyzed.sl" to your python projects
	
    Some IDEs might complain that the import fails, but if you run the python script inside a terminal it should work.

5. Hopefully done! Run detect_camera.py to check.

---

### useful Links

Python API documentation: https://www.stereolabs.com/docs/api/python/

Tutorials for can be found here: https://www.stereolabs.com/docs/tutorials/