
This is repo is a compound collections of projects involved in the creation of a mechanical keyboard. Consists of AVR programming, and python GUI program to remap keys with ease.

NOTE: The USBaspLoader is an open source bootloader that allows us to reprogram the MCU via USB connection rather than the programmer itself. All credit is also given to u/baerwolf. We simply adjusted the given files to match with our hardware, which was the USBtiny programmer and ATMEGA328P MCU. 

[Bootloader](https://github.com/hsgw/USBaspLoader/tree/plaid)

### Milestones

- [x] Researching which compiler to use for programming the ATMega microprocessors

- [x]_referencing the code from qmk_firmware_
- [ ] Create a working prototype for the testing code
- [ ] Iterate the code to work for multiple key switches
- [ ] Design a custom PCB for the phase two prototype
- [ ] Test the code and circuitry on the second prototype
- [x] Learn to code python
- [x] learn to make a simple python app
- [ ] Develop a prototype GUI
- [ ] Research ways to integrate the python application with the AVR programming
- [ ] Develop a proper over UI design for the application
- [ ] ...

###### Details about this repo:
As of now, this repo is intended to show the progress done on the project and to be used as a reference point for not only us but for the community who might have the same difficulties as us in following the guides provided online. Because this is our first time with an interdisciplinary project this big, we are expecting a lot of revisions down the road and possibilities of abandoning some original concepts. Understanding that, we want to state that our intentions with this project the passion and interests in our hobbies. There's also a bonus of being able to develop teamwork, communication, research and design, troubleshooting, and problem-solving skills, along with various other technical skills.

###### Resources:
[QMK_Firmware](https://github.com/qmk/qmk_firmware)

[Bootloader](https://github.com/hsgw/USBaspLoader/tree/plaid)

[AtmelStudio 7(for programing the ATMega)](https://www.microchip.com/mplab/avr-support/atmel-studio-7)
 
[Handwiring Keyboard Guide](https://beta.docs.qmk.fm/for-makers-and-modders/hand_wire)

[Understanding GMK](https://beta.docs.qmk.fm/for-a-deeper-understanding/understanding_qmk)

[AVR Pocket Programmer Guide]([Understanding GMK](https://beta.docs.qmk.fm/for-a-deeper-understanding/understanding_qmk)

---

###### Log (Helping us keep track of where we):
Seems that the most popular guides on making mechanical keyboards are recommending WinAVR, but it seems that the program is a bit outdated, and not as decked out as Atmelstudio 7. 
##### 11/21/2019:
We discovered that we can't do anything with the Atmega chips while using the pickit 3. There are no compatibility in the two resources. We're going to see if we can use the arduinos to burn a bootloader onto the Atmega chip.
##### 11/10/2019:
Because our Atmegas is produced by Atmel, we're using that for programming our bootloader, however, due to the limited resource, we're going to have to hope that we could use the Pickit 3 as a compiler for our bootloader. So the process for the bootloader consists of **Downloading the USBaspLoader, modifying it for our selected microprocessor, and burning it onto the chip using Atmel Studio 7 and PicKit 3**.

The provided Firmware which we'll need to flash onto the chip, after burning the bootloader, has a very nice template that makes it very intuitive to follow and configure. The plan is to be able to reconstruct the template so that we could **parse the text from the python app, and Rewrite it with the user's input**. However, we are still researching how to reupload the firmware onto the chip through a USB cable.

##### 12/11/2019: 
We decided to order the ATMEL 51 AVR USB ISP ASP Microcontroller Programmer in order to actually program the ATMEGA chip itself. In the meantime of waiting for it to arrive, we decided attempt to burn the UWSBaspLoader boot loader onto the MCU through an Arduino board. After getting the bootloader onto the MCU, we will then flash the opensource QMK firmware.

After doing so, we will then begin actually building a phsyical 4 key prototype of our keyboard.

##### 12/30/2019: 
Using the AVR Pocket Programmer, we connected the jumper to the coresponding ISP pins on the Arduino Uno which still had the ATMEGA328P attatched. Our initial difficulty was getting Windows to recognize the programmer, which we later realized was because of a faulty cable that came along with the programmer. We proceeded to use Zadig to install the needed drivers (libusb) for the device.

To actually flash the USBaspLoader onto the MCU, we needed to be in the directory of the extracted folder. Initially, I used Ubuntu to do this but AVRDUDE was having difficulty recognizing the device. I then switched to Command Prompt and was able to succesfully flash the bootlader on using the make command, make flash, and make fuse.I also had to change a couple settings in the Makefile.inc file to fit with our corresponding hardware.
##### 3/07/2020: 
Successfully created new keybaord directory using util/new_keyboard.sh commnad.
##### 4/5/2020: 
All of keympas and files succesfully compiles. Flashed USBaspLoader onto 32U MCU, along with completed firmware flashing. 
General and simple application was also updated using python, and I was able to retrieve users directory path to firmware folder. More implementation on program interface and editing c files will need to be done.  
