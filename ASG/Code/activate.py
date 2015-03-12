import os
import shutil


def activate(aircraft):
    """This function activates an aircraft in subfolders Pre-flight and Mid-flight.
Input aircraft must be a string. Currently available aircraft: 'imaginary.py'.
    """

    folders = ('Pre-flight', 'Mid-flight')       # folders to write in
    from_ac = os.path.join('available_aircraft', aircraft)

    for folder in folders:
        to_ac = os.path.join(folder, 'active_aircraft.py')
        shutil.copyfile(from_ac, to_ac)          # copy file and overwrite old.

    return None
