import unittest
import numpy as np
import sys
import os

Add src directory to Python path

sys.path.insert(
0,
os.path.abspath(
os.path.join(os.path.dirname(file), "../src")
)
)

from fm_signal_simulator import generate_fm_signal

class TestFMSignal(unittest.TestCase):

def setUp(self):

    self.fc = 10_000
    self.fm = 1_000
    self.Ac = 1.0
    self.Am = 1.0
    self.delta_f = 5_000
    self.fs = 200_000
    self.duration = 0.005

    (
        self.t,
        self.message,
        self.carrier,
        self.fm_signal,
        self.beta
    ) = generate_fm_signal(
        self.fc,
        self.fm,
        self.Ac,
        self.Am,
        self.delta_f,
        self.fs,
        self.duration
    )

def test_modulation_index(self):

    expected_beta = self.delta_f / self.fm

    self.assertAlmostEqual(
        self.beta,
        expected_beta
    )

def test_signal_length(self):

    expected_length = int(
        self.fs * self.duration
    )

    self.assertEqual(
        len(self.t),
        expected_length
    )

def test_message_amplitude(self):

    self.assertLessEqual(
        np.max(np.abs(self.message)),
        self.Am + 0.01
    )

def test_carrier_amplitude(self):

    self.assertLessEqual(
        np.max(np.abs(self.carrier)),
        self.Ac + 0.01
    )

def test_fm_signal_amplitude(self):

    self.assertLessEqual(
        np.max(np.abs(self.fm_signal)),
        self.Ac + 0.01
    )

def test_invalid_frequency(self):

    with self.assertRaises(ValueError):

        generate_fm_signal(
            carrier_frequency=-10000,
            message_frequency=self.fm,
            carrier_amplitude=self.Ac,
            message_amplitude=self.Am,
            frequency_deviation=self.delta_f,
            sampling_frequency=self.fs,
            duration=self.duration
        )


if name == "main":
unittest.main()
