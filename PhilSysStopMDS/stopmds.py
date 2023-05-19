import os
import subprocess
import psutil
import win32serviceutil

def is_service_running(service_name):
    for service in psutil.win_service_iter():
        if service_name.lower() == service.name().lower():
            if service.status() == psutil.STATUS_RUNNING:
                return True
    return False

def stop_service(service_name):
    try:
        win32serviceutil.StopService(service_name)
        print(f"{service_name} service stopped successfully.")
    except Exception as e:
        print(f"Error stopping {service_name} service: {e}")

def checkMLS():
    if is_service_running("Multiprotect License Service"):
        print("Multiprotect License Service: RUNNING")
    else:
        print("Multiprotect License Service: STOPPED/See remarks^")

def checkFace():
    if is_service_running("NextFaceService"):
        print("NextFaceService: RUNNING")
    else:
        print("NextFaceService: STOPPED/See remarks^")

    if is_service_running("FaceMDSService") or is_service_running("FaceMDService"):
        print("FaceMDService: RUNNING")
    else:
        print("FaceMDService: STOPPED/See remarks^")


def checkIris():
    if is_service_running("NextIrisService"):
        print("NextIrisService: RUNNING")
    else:
        print("NextFaceService: STOPPED/See remarks^")

def checkFingerprint():
    if is_service_running("Thales_Finger_MDS"):
        print("Thales_Finger_MDS: RUNNING")
    else:
        print("Thales_Finger_MDS: STOPPED/See remarks^")

def stopMLS():
    stop_service("Multiprotect License Service")

def stopFace():
    stop_service("NextFaceService")
    stop_service("FaceMDSService")
    stop_service("FaceMDService")

def stopIris():
    stop_service("NextIrisService")

def stopFingerprint():
    stop_service("Thales_Finger_MDS")

while True:
    choice = str(input("""\n[PHILSYS SERVICE SUSPENDER]
*DISCLAIMER: Make sure you "Run as Administrator". Service names derived from actual and not description.

        Service Menu

                [1] Check status
                [2] Stop "Multiprotect License Service"
                [3] Stop "NextFaceService/FaceMDService"
                [4] Stop "NextIrisService"
                [5] Stop "Thales_Finger_MDS"
                [6] Stop "NextFaceService/FaceMDService"; "NextIrisService"; "Thales_Finger_MDS"
                [7] Exit

        Enter choice >>> """))

    if choice == '1':
        print("\n") #line break purposes
        checkMLS()
        checkFace()
        checkIris()
        checkFingerprint()              
       
    elif choice == '2':
        print("\n") #line break purposes
        stopMLS()
        checkMLS()
       
    elif choice == '3':
        print("\n") #line break purposes
        stopFace()
        checkFace()

    elif choice == '4':
        print("\n") #line break purposes
        stopIris()
        checkIris()
        
    elif choice == '5':
        print("\n") #line break purposes
        stopFingerprint()
        checkFingerprint()

    elif choice == '6':
        print("\n") #line break purposes
        stopFace()
        stopIris()
        stopFingerprint()
        print("\n") #line break purposes
        checkMLS()
        checkFace()
        checkIris()
        checkFingerprint()  

    elif choice == '7':
        print("\n") #line break purposes
        quit()
        break
    else:
        #raise Exception
        continue