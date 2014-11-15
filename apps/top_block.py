#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sat Nov 15 12:18:38 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy as np
import sip
import sys
import threading
import time

from distutils.version import StrictVersion
class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.offset_tune_freq = offset_tune_freq = -10E3
        self.band_freq = band_freq = 7.055E6
        self.usrp_clk_rate = usrp_clk_rate = 200E6
        self.usrp_ask_freq = usrp_ask_freq = band_freq+offset_tune_freq
        self.usrp_DDC_freq = usrp_DDC_freq = np.round(usrp_ask_freq/usrp_clk_rate* 2**32)/2**32 * usrp_clk_rate
        self.fine_tuner_freq = fine_tuner_freq = 0
        self.coarse_tuner_freq = coarse_tuner_freq = 0
        self.samp_rate = samp_rate = 250000
        self.lo_freq = lo_freq = usrp_DDC_freq + coarse_tuner_freq + fine_tuner_freq - offset_tune_freq
        self.record_check_box = record_check_box = False
        self.file_name_string = file_name_string = str(int(time.mktime(time.gmtime())))+"UTC_"+'{:.6f}'.format(lo_freq)+"Hz"+"_"+str(int(samp_rate/100))+"sps"+".raw"
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.file_name = file_name = file_name_string if record_check_box==True else "/dev/null"
        self.volume = volume = 5.0
        self.rx_power_label = rx_power_label = '{:.1f}'.format(variable_function_probe_0)
        self.lo_freq_label = lo_freq_label = '{:.6f}'.format(lo_freq)
        self.gain_offset_dB = gain_offset_dB = 18.86
        self.filter_taps = filter_taps = firdes.low_pass(1.0,2.5,0.1,0.02,firdes.WIN_HAMMING)
        self.filename_label = filename_label = file_name
        self.cw_filter_bw = cw_filter_bw = 1000
        self.RX_power_offset_dB = RX_power_offset_dB = -35.2

        ##################################################
        # Blocks
        ##################################################
        self._volume_layout = Qt.QVBoxLayout()
        self._volume_knob = Qwt.QwtKnob()
        self._volume_knob.setRange(0, 10.0, 1.0)
        self._volume_knob.setValue(self.volume)
        self._volume_knob.valueChanged.connect(self.set_volume)
        self._volume_layout.addWidget(self._volume_knob)
        self._volume_label = Qt.QLabel("Volume")
        self._volume_label.setAlignment(Qt.Qt.AlignTop | Qt.Qt.AlignHCenter)
        self._volume_layout.addWidget(self._volume_label)
        self.top_grid_layout.addLayout(self._volume_layout, 5,6,1,1)
        self._cw_filter_bw_options = (100, 500, 1000, )
        self._cw_filter_bw_labels = ("100 Hz", "500 Hz", "1 kHz", )
        self._cw_filter_bw_tool_bar = Qt.QToolBar(self)
        self._cw_filter_bw_tool_bar.addWidget(Qt.QLabel("CW Filter BW"+": "))
        self._cw_filter_bw_combo_box = Qt.QComboBox()
        self._cw_filter_bw_tool_bar.addWidget(self._cw_filter_bw_combo_box)
        for label in self._cw_filter_bw_labels: self._cw_filter_bw_combo_box.addItem(label)
        self._cw_filter_bw_callback = lambda i: Qt.QMetaObject.invokeMethod(self._cw_filter_bw_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._cw_filter_bw_options.index(i)))
        self._cw_filter_bw_callback(self.cw_filter_bw)
        self._cw_filter_bw_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_cw_filter_bw(self._cw_filter_bw_options[i]))
        self.top_grid_layout.addWidget(self._cw_filter_bw_tool_bar, 5,5,1,1)
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        def _variable_function_probe_0_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (5))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "addr=192.168.40.2")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec("B:A", 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(usrp_ask_freq, 0)
        self.uhd_usrp_source_0.set_gain(6, 0)
        self._rx_power_label_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._rx_power_label_formatter = None
        else:
          self._rx_power_label_formatter = lambda x: x
        
        self._rx_power_label_tool_bar.addWidget(Qt.QLabel("RX Power (dBm)"+": "))
        self._rx_power_label_label = Qt.QLabel(str(self._rx_power_label_formatter(self.rx_power_label)))
        self._rx_power_label_tool_bar.addWidget(self._rx_power_label_label)
        self.top_grid_layout.addWidget(self._rx_power_label_tool_bar, 4,7,1,1)
          
        _record_check_box_check_box = Qt.QCheckBox("Record")
        self._record_check_box_choices = {True: True, False: False}
        self._record_check_box_choices_inv = dict((v,k) for k,v in self._record_check_box_choices.iteritems())
        self._record_check_box_callback = lambda i: Qt.QMetaObject.invokeMethod(_record_check_box_check_box, "setChecked", Qt.Q_ARG("bool", self._record_check_box_choices_inv[i]))
        self._record_check_box_callback(self.record_check_box)
        _record_check_box_check_box.stateChanged.connect(lambda i: self.set_record_check_box(self._record_check_box_choices[bool(i)]))
        self.top_grid_layout.addWidget(_record_check_box_check_box, 6,5,1,1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=2500,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	usrp_DDC_freq, #fc
        	samp_rate, #bw
        	"Band Waterfall", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        
        if complex == type(float()):
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, -70)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 4,0,3,5)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	lo_freq, #fc
        	samp_rate/100, #bw
        	str(samp_rate/100) + " Hz Channel Spectrum", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-120, -70)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 0,5,3,5)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	usrp_DDC_freq, #fc
        	samp_rate, #bw
        	"Band Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-110, -60)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,3,5)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/100, 0.9*cw_filter_bw, 0.1*cw_filter_bw, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	10**(gain_offset_dB/20), samp_rate, 100E3, 20E3, firdes.WIN_HAMMING, 6.76))
        self._lo_freq_label_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._lo_freq_label_formatter = None
        else:
          self._lo_freq_label_formatter = lambda x: x
        
        self._lo_freq_label_tool_bar.addWidget(Qt.QLabel("LO Freq (Hz)"+": "))
        self._lo_freq_label_label = Qt.QLabel(str(self._lo_freq_label_formatter(self.lo_freq_label)))
        self._lo_freq_label_tool_bar.addWidget(self._lo_freq_label_label)
        self.top_grid_layout.addWidget(self._lo_freq_label_tool_bar, 4,6,1,1)
          
        self.hilbert_fc_0_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(10, (filter_taps), lo_freq - usrp_DDC_freq, samp_rate)
        self.fir_filter_xxx_0_0_0 = filter.fir_filter_ccc(10, (filter_taps))
        self.fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self._fine_tuner_freq_layout = Qt.QVBoxLayout()
        self._fine_tuner_freq_tool_bar = Qt.QToolBar(self)
        self._fine_tuner_freq_layout.addWidget(self._fine_tuner_freq_tool_bar)
        self._fine_tuner_freq_tool_bar.addWidget(Qt.QLabel("Fine Tuner (Hz)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._fine_tuner_freq_counter = qwt_counter_pyslot()
        self._fine_tuner_freq_counter.setRange(-500, 500, 1)
        self._fine_tuner_freq_counter.setNumButtons(2)
        self._fine_tuner_freq_counter.setValue(self.fine_tuner_freq)
        self._fine_tuner_freq_tool_bar.addWidget(self._fine_tuner_freq_counter)
        self._fine_tuner_freq_counter.valueChanged.connect(self.set_fine_tuner_freq)
        self._fine_tuner_freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._fine_tuner_freq_slider.setRange(-500, 500, 1)
        self._fine_tuner_freq_slider.setValue(self.fine_tuner_freq)
        self._fine_tuner_freq_slider.setMinimumWidth(200)
        self._fine_tuner_freq_slider.valueChanged.connect(self.set_fine_tuner_freq)
        self._fine_tuner_freq_layout.addWidget(self._fine_tuner_freq_slider)
        self.top_grid_layout.addLayout(self._fine_tuner_freq_layout, 3,5,1,5)
        self._filename_label_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._filename_label_formatter = None
        else:
          self._filename_label_formatter = lambda x: x
        
        self._filename_label_tool_bar.addWidget(Qt.QLabel("File Name"+": "))
        self._filename_label_label = Qt.QLabel(str(self._filename_label_formatter(self.filename_label)))
        self._filename_label_tool_bar.addWidget(self._filename_label_label)
        self.top_grid_layout.addWidget(self._filename_label_tool_bar, 6,6,1,3)
          
        self._coarse_tuner_freq_layout = Qt.QVBoxLayout()
        self._coarse_tuner_freq_tool_bar = Qt.QToolBar(self)
        self._coarse_tuner_freq_layout.addWidget(self._coarse_tuner_freq_tool_bar)
        self._coarse_tuner_freq_tool_bar.addWidget(Qt.QLabel("Coarse Tuner (Hz)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._coarse_tuner_freq_counter = qwt_counter_pyslot()
        self._coarse_tuner_freq_counter.setRange(-samp_rate/2, samp_rate/2, 100)
        self._coarse_tuner_freq_counter.setNumButtons(2)
        self._coarse_tuner_freq_counter.setValue(self.coarse_tuner_freq)
        self._coarse_tuner_freq_tool_bar.addWidget(self._coarse_tuner_freq_counter)
        self._coarse_tuner_freq_counter.valueChanged.connect(self.set_coarse_tuner_freq)
        self._coarse_tuner_freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._coarse_tuner_freq_slider.setRange(-samp_rate/2, samp_rate/2, 100)
        self._coarse_tuner_freq_slider.setValue(self.coarse_tuner_freq)
        self._coarse_tuner_freq_slider.setMinimumWidth(50)
        self._coarse_tuner_freq_slider.valueChanged.connect(self.set_coarse_tuner_freq)
        self._coarse_tuner_freq_layout.addWidget(self._coarse_tuner_freq_slider)
        self.top_grid_layout.addLayout(self._coarse_tuner_freq_layout, 3,0,1,5)
        self.blocks_null_sink_1_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_1_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, RX_power_offset_dB)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(500)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, file_name, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_1_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self._band_freq_options = [1.84E6, 3.598E6, 7.055E6, 2.5E6, 5.0E6, 10.0E6]
        self._band_freq_labels = ["160m", "80m", "40m", "2.5 MHz", "5 MHz", "10 MHz"]
        self._band_freq_tool_bar = Qt.QToolBar(self)
        self._band_freq_tool_bar.addWidget(Qt.QLabel("Band"+": "))
        self._band_freq_combo_box = Qt.QComboBox()
        self._band_freq_tool_bar.addWidget(self._band_freq_combo_box)
        for label in self._band_freq_labels: self._band_freq_combo_box.addItem(label)
        self._band_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._band_freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._band_freq_options.index(i)))
        self._band_freq_callback(self.band_freq)
        self._band_freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_band_freq(self._band_freq_options[i]))
        self.top_grid_layout.addWidget(self._band_freq_tool_bar, 4,5,1,1)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/100, analog.GR_COS_WAVE, 600, 1, 0)
        self.analog_agc3_xx_0 = analog.agc3_cc(1e-1, 1e-4, volume/100, 1, 1)
        self.analog_agc3_xx_0.set_max_gain(2**16)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.fir_filter_xxx_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.fir_filter_xxx_0_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.analog_agc3_xx_0, 0), (self.blocks_complex_to_float_1_0, 0))
        self.connect((self.fir_filter_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_null_sink_1_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_1_0, 0))
        self.connect((self.blocks_complex_to_float_1_0, 1), (self.hilbert_fc_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_1_0, 0), (self.hilbert_fc_0_0, 0))
        self.connect((self.hilbert_fc_0_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_offset_tune_freq(self):
        return self.offset_tune_freq

    def set_offset_tune_freq(self, offset_tune_freq):
        self.offset_tune_freq = offset_tune_freq
        self.set_lo_freq(self.usrp_DDC_freq + self.coarse_tuner_freq + self.fine_tuner_freq - self.offset_tune_freq)
        self.set_usrp_ask_freq(self.band_freq+self.offset_tune_freq)

    def get_band_freq(self):
        return self.band_freq

    def set_band_freq(self, band_freq):
        self.band_freq = band_freq
        self.set_usrp_ask_freq(self.band_freq+self.offset_tune_freq)
        self._band_freq_callback(self.band_freq)

    def get_usrp_clk_rate(self):
        return self.usrp_clk_rate

    def set_usrp_clk_rate(self, usrp_clk_rate):
        self.usrp_clk_rate = usrp_clk_rate
        self.set_usrp_DDC_freq(np.round(self.usrp_ask_freq/self.usrp_clk_rate* 2**32)/2**32 * self.usrp_clk_rate)

    def get_usrp_ask_freq(self):
        return self.usrp_ask_freq

    def set_usrp_ask_freq(self, usrp_ask_freq):
        self.usrp_ask_freq = usrp_ask_freq
        self.set_usrp_DDC_freq(np.round(self.usrp_ask_freq/self.usrp_clk_rate* 2**32)/2**32 * self.usrp_clk_rate)
        self.uhd_usrp_source_0.set_center_freq(self.usrp_ask_freq, 0)

    def get_usrp_DDC_freq(self):
        return self.usrp_DDC_freq

    def set_usrp_DDC_freq(self, usrp_DDC_freq):
        self.usrp_DDC_freq = usrp_DDC_freq
        self.set_lo_freq(self.usrp_DDC_freq + self.coarse_tuner_freq + self.fine_tuner_freq - self.offset_tune_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_DDC_freq)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.usrp_DDC_freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.usrp_DDC_freq, self.samp_rate)

    def get_fine_tuner_freq(self):
        return self.fine_tuner_freq

    def set_fine_tuner_freq(self, fine_tuner_freq):
        self.fine_tuner_freq = fine_tuner_freq
        self.set_lo_freq(self.usrp_DDC_freq + self.coarse_tuner_freq + self.fine_tuner_freq - self.offset_tune_freq)
        Qt.QMetaObject.invokeMethod(self._fine_tuner_freq_counter, "setValue", Qt.Q_ARG("double", self.fine_tuner_freq))
        Qt.QMetaObject.invokeMethod(self._fine_tuner_freq_slider, "setValue", Qt.Q_ARG("double", self.fine_tuner_freq))

    def get_coarse_tuner_freq(self):
        return self.coarse_tuner_freq

    def set_coarse_tuner_freq(self, coarse_tuner_freq):
        self.coarse_tuner_freq = coarse_tuner_freq
        self.set_lo_freq(self.usrp_DDC_freq + self.coarse_tuner_freq + self.fine_tuner_freq - self.offset_tune_freq)
        Qt.QMetaObject.invokeMethod(self._coarse_tuner_freq_counter, "setValue", Qt.Q_ARG("double", self.coarse_tuner_freq))
        Qt.QMetaObject.invokeMethod(self._coarse_tuner_freq_slider, "setValue", Qt.Q_ARG("double", self.coarse_tuner_freq))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_file_name_string(str(int(time.mktime(time.gmtime())))+"UTC_"+'{:.6f}'.format(self.lo_freq)+"Hz"+"_"+str(int(self.samp_rate/100))+"sps"+".raw")
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/100)
        self.low_pass_filter_0.set_taps(firdes.low_pass(10**(self.gain_offset_dB/20), self.samp_rate, 100E3, 20E3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/100, 0.9*self.cw_filter_bw, 0.1*self.cw_filter_bw, firdes.WIN_BLACKMAN, 6.76))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.lo_freq, self.samp_rate/100)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.usrp_DDC_freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.usrp_DDC_freq, self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_lo_freq(self):
        return self.lo_freq

    def set_lo_freq(self, lo_freq):
        self.lo_freq = lo_freq
        self.set_file_name_string(str(int(time.mktime(time.gmtime())))+"UTC_"+'{:.6f}'.format(self.lo_freq)+"Hz"+"_"+str(int(self.samp_rate/100))+"sps"+".raw")
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_DDC_freq)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.lo_freq, self.samp_rate/100)
        self.set_lo_freq_label(self._lo_freq_label_formatter('{:.6f}'.format(self.lo_freq)))

    def get_record_check_box(self):
        return self.record_check_box

    def set_record_check_box(self, record_check_box):
        self.record_check_box = record_check_box
        self.set_file_name(self.file_name_string if self.record_check_box==True else "/dev/null")
        self._record_check_box_callback(self.record_check_box)

    def get_file_name_string(self):
        return self.file_name_string

    def set_file_name_string(self, file_name_string):
        self.file_name_string = file_name_string
        self.set_file_name(self.file_name_string if self.record_check_box==True else "/dev/null")

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0
        self.set_rx_power_label(self._rx_power_label_formatter('{:.1f}'.format(self.variable_function_probe_0)))

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.blocks_file_sink_0.open(self.file_name)
        self.set_filename_label(self._filename_label_formatter(self.file_name))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.analog_agc3_xx_0.set_reference(self.volume/100)
        Qt.QMetaObject.invokeMethod(self._volume_knob, "setValue", Qt.Q_ARG("double", self.volume))

    def get_rx_power_label(self):
        return self.rx_power_label

    def set_rx_power_label(self, rx_power_label):
        self.rx_power_label = rx_power_label
        Qt.QMetaObject.invokeMethod(self._rx_power_label_label, "setText", Qt.Q_ARG("QString", str(self.rx_power_label)))

    def get_lo_freq_label(self):
        return self.lo_freq_label

    def set_lo_freq_label(self, lo_freq_label):
        self.lo_freq_label = lo_freq_label
        Qt.QMetaObject.invokeMethod(self._lo_freq_label_label, "setText", Qt.Q_ARG("QString", str(self.lo_freq_label)))

    def get_gain_offset_dB(self):
        return self.gain_offset_dB

    def set_gain_offset_dB(self, gain_offset_dB):
        self.gain_offset_dB = gain_offset_dB
        self.low_pass_filter_0.set_taps(firdes.low_pass(10**(self.gain_offset_dB/20), self.samp_rate, 100E3, 20E3, firdes.WIN_HAMMING, 6.76))

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.filter_taps))
        self.fir_filter_xxx_0_0_0.set_taps((self.filter_taps))

    def get_filename_label(self):
        return self.filename_label

    def set_filename_label(self, filename_label):
        self.filename_label = filename_label
        Qt.QMetaObject.invokeMethod(self._filename_label_label, "setText", Qt.Q_ARG("QString", str(self.filename_label)))

    def get_cw_filter_bw(self):
        return self.cw_filter_bw

    def set_cw_filter_bw(self, cw_filter_bw):
        self.cw_filter_bw = cw_filter_bw
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/100, 0.9*self.cw_filter_bw, 0.1*self.cw_filter_bw, firdes.WIN_BLACKMAN, 6.76))
        self._cw_filter_bw_callback(self.cw_filter_bw)

    def get_RX_power_offset_dB(self):
        return self.RX_power_offset_dB

    def set_RX_power_offset_dB(self, RX_power_offset_dB):
        self.RX_power_offset_dB = RX_power_offset_dB

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
