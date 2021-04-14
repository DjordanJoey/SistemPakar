# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 04:07:39 2021

@author: HP
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


jarak = ctrl.Antecedent(np.arange(0, 11, 1), 'jarak')
waktu = ctrl.Antecedent(np.arange(0, 11, 1), 'waktu')
kecepatan = ctrl.Consequent(np.arange(0, 26, 1), 'kecepatan')


jarak.automf(3)
waktu.automf(3)


kecepatan['slow'] = fuzz.trimf(kecepatan.universe, [0, 0, 13])
kecepatan['medium'] = fuzz.trimf(kecepatan.universe, [0, 13, 25])
kecepatan['fast'] = fuzz.trimf(kecepatan.universe, [13, 25, 25])

jarak.view()
waktu.view()
kecepatan.view()

rule1 = ctrl.Rule(jarak['poor'] | waktu['poor'], kecepatan['slow'])
rule2 = ctrl.Rule(jarak['average'] | waktu['average'], kecepatan['medium'])
rule3 = ctrl.Rule(jarak['good'] | waktu['good'], kecepatan['fast'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['jarak'] = 7.0
tipping.input['waktu'] = 7.0


tipping.compute()

print ('Kecepatan yang optimal', tipping.output['kecepatan'])
kecepatan.view(sim=tipping)