#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This file is part of the Wapiti project (https://wapiti-scanner.github.io)
# Copyright (C) 2022 Nicolas SURRIBAS
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
from datetime import datetime
from random import choice

from wapitiCore import WAPITI_VERSION
from wapitiCore.moon import phase
from asciistuff import Banner, Lolcat


    print(Fore.BLUE + Style.BRIGHT + str(Lolcat(Banner("BOSCH"))))
    print(f"MS/ECE2 Pentest as Service (bosch.co.in)")
    print("For a detailed Pentest report kindly contact MS/ECE2")
    moon_phase = phase()
    if moon_phase == "full":
        print("[*] You are lucky! Full moon tonight.")
    elif moon_phase == "new":
        print("[*] Be careful! New moon tonight.")

    if datetime.now().weekday() == 4:
        if datetime.now().day == 13:
            print("[*] Watch out! Bad things can happen on Friday the 13th.")
        elif datetime.now().month == 8 and datetime.now().day < 8:
            print("[*] Today is International Beer Day!")

    if datetime.now().month == 5 and datetime.now().day == 4:
        print("[*] May the force be with you!")
    elif datetime.now().month == datetime.now().day == 1:
        print("[*] Happy new year!")
    elif datetime.now().month == 12 and datetime.now().day == 25:
        print("[*] Merry christmas!")
    elif datetime.now().month == 3 and datetime.now().day == 31:
        print("[*] Today is world backup day! Is your data safe?")
