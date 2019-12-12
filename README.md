# CustomKeyboard
This is repo is a compound collections of projects involved in the creation of a mechanical keyboard. Consists of AVR programing, and pythong GUI program to remap keys with ease.
### Milestones

- [x] Researching which compiler to use for programming the ATMega microprocessors
- [ ] Make a testing code for the ATMega328p that registers a keypress (from a mechanical keyboard switch)
  - _referencing the code from qmk_firmware_
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

---

###### Log (Helping us keep track of where we):
Seems that the most popular guides on making mechanical keyboards are recommending WinAVR, but it seems that the program is a bit outdated, and not as decked out as Atmelstudio 7. 
##### 11/21/2019:
We discovered that we can't do anything with the Atmega chips while using the pickit 3. There are no compatibility in the two resources. We're going to see if we can use the arduinos to burn a bootloader onto the Atmega chip.
##### 11/10/2019:
Because our Atmegas is produced by Atmel, we're using that for programming our bootloader, however, due to the limited resource, we're going to have to hope that we could use the Pickit 3 as a compiler for our bootloader. So the process for the bootloader consists of **Downloading the USBaspLoader, modifying it for our selected microprocessor, and burning it onto the chip using Atmel Studio 7 and PicKit 3**.

The provided Firmware which we'll need to flash onto the chip, after burning the bootloader, has a very nice template that makes it very intuitive to follow and configure. The plan is to be able to reconstruct the template so that we could **parse the text from the python app, and Rewrite it with the user's input**. However, we are still researching how to reupload the firmware onto the chip through a USB cable.

##### 12/11/2019: 
We decided to order the ATMEL 51 AVR USB ISP ASP Microcontroller Programmer in order to actually program the ATMEGA chip itself. In the meantime of waiting for it to arrive, we decided to try burn the UWSBaspLoader boot loader onto the MCU. After getting the bootloader onto the MCU, we will then flash the opensource QMK firmware.

After doing so, we will then begin actually building a phsyical 4 key prototype of our keyboard. 
