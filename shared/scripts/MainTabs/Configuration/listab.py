# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from configurationtab import ConfigurationTab

class LisTab(ConfigurationTab):
    
    def __init__(self):
        self.object_symbol = ":Configuration.LIS_TabProxy"
        self.lis_general_label_symbol = ":LIS_JPanel"
        self.lis_astm_label_symbol = ":LIS_JPanel_5"
        self.lis_hl7_label_symbol = ":LIS_JPanel_9"
        self.lis_tcp_ip_connection_label_symbol = ":LIS_JPanel_8"

        #LIS General
        self.lis_enabled_checkbox_symbol = ":LIS. _JCheckBox"
        self.lis_encoding_astm_radiobutton_symbol = ":LIS.ASTM_JRadioButton"
        self.lis_encoding_hl7_radiobutton_symbol = ":LIS.HL7_JRadioButton"
        self.lis_encoding_lis_simulator_radiobutton_symbol = ":LIS.LIS Simulator_JRadioButton"
        self.lis_downloadmode_order_download_radiobutton_symbol = ":LIS.Work Order Download_JRadioButton"
        self.lis_downloadmode_host_query_radiobutton_symbol = ":LIS.Host-Query_JRadioButton"
        self.lis_historical_lookup_checkbox_symbol =":LIS.Enabled_JCheckBox"
        self.purge_pending_orders_textfield_symbol = ":LIS_JTextField"
        self.sender_id_textfield_symbol = ":LIS_JTextField_2"
        self.receiver_id_textfield_symbol = ":LIS_JTextField_3"
        self.mode_production_radiobutton_symbol = ":LIS.Production_JRadioButton"
        self.mode_training_radiobutton_symbol = ":LIS.Training_JRadioButton"
        self.mode_debug_radiobutton_symbol = ":LIS.Debug_JRadioButton"
        
        #LIS ASTM
        self.query_wait_time_textfield_symbol = ":LIS_JTextField_4"
        self.message_retry_count_textfield_symbol = ":LIS_JTextField_5"
        self.message_retry_delay_textfield_symbol = ":LIS_JTextField_6"
        self.socket_retry_count_textfield_symbol = ":LIS_JTextField_7"
        self.socket_retry_delay_textfield_symbol = ":LIS_JTextField_8"
        
        #LIS HL7
        self.reverse_ae_and_ar_meanings_checkbox_symbol = ":LIS.Enabled_JCheckBox_2"
        self.retransmit_on_receiver_reject_checkbox_symbol = ":LIS.Enabled_JCheckBox_3"
        self.retry_count_textfield_symbol = ":LIS_JTextField_9"
        self.retry_delay_textfield_symbol = ":LIS_JTextField_10"
        
        #LIS TCP/IP Connection
        self.remote_address_textfield_symbol = ":LIS_JTextField_11"
        self.port_textfield_symbol = ":LIS_JTextField_12"
        self.listen_on_port_symbol = ":LIS_JTextField_13"
        self.timeout_textfield_symbol = ":LIS_JTextField_14"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    #Confirm that the following sections are displayed:
    #-LIS General
    #-LIS ASTM
    #-LIS HL7
    #-LIS TCP / IP Connection        
    def confirmDefaultControlsAndValues(self):
        test.verify(self.getLisLabel(self.lis_general_label_symbol) == "LIS General", "Confirm that LIS General is the name of the first section on the LIS tab")
        test.verify(self.getLisLabel(self.lis_astm_label_symbol) == "LIS ASTM","Confirm that LIS ASTM is the name of the second section on the LIS tab")
        test.verify(self.getLisLabel(self.lis_hl7_label_symbol) == "LIS HL7", "Confirm that LIS HL7 is the name of the third section on the LIS tab")
        test.verify(self.getLisLabel(self.lis_tcp_ip_connection_label_symbol) == "LIS TCP/IP Connection", "Confirm that LIS TCP/IP is the name of the fourth section on the LIS tab")
        
    def getLisLabel(self,object_symbol):
        label_object = findObject(object_symbol)
        field = label_object.getClass().getDeclaredField("label")
        field.setAccessible(True)
        label = field.get(label_object)
        return label.text
    
    #203. Review the default settings under the LIS General section
    #Confirm each parameters in the LIS General section are defaulted as so: 
    #-LIS Enabled checkbox: (checked)
    #-LIS Encoding combobox: NONE (selected by default)
    #-LIS Encoding combobox has the following values: NONE, ASTM, HL7
    #-LIS Download Mode combobox: ORDER_ DOWNLOAD
    #-LIS Download Mode combobox has the following values: ORDER_DOWNLOAD, HOST_QUERY
    #-LIS Historical Lookup checkbox: (checked)
    #-Purge Pending Orders text field: 999 days
    #-Sender ID text field: Bloodhound
    #-Receiver ID text field: LIS
    #-Mode combobox: DEBUG
    #-Mode combobox has the following values: DEBUG, PRODUCTION, TRAINING
    def confirmLISGeneralSectionForDefaultControlsAndValues(self):
        lis_enabled_checkbox = findObject(self.lis_enabled_checkbox_symbol)
        lis_historical_checkbox = findObject(self.lis_historical_lookup_checkbox_symbol)
        purge_pending_orders = findObject(self.purge_pending_orders_textfield_symbol)
        sender_id = findObject(self.sender_id_textfield_symbol)
        receiver_id = findObject(self.receiver_id_textfield_symbol)

        #-LIS Enabled checkbox: (checked)
        test.verify(lis_enabled_checkbox.enabled == True, "Confirm that the Lis Enabled checkbox is checked by default")
        #-LIS Encoding ASTM Radio Button
        Controls.confirmRadioButton(self,self.lis_encoding_astm_radiobutton_symbol, "enabled", "un-selected","ASTM")
        #-LIS Encoding HL7 Radio Button
        Controls.confirmRadioButton(self,self.lis_encoding_hl7_radiobutton_symbol, "enabled", "un-selected","HL7")
        #-LIS Encoding LIS Simulator Radio Button
        Controls.confirmRadioButton(self,self.lis_encoding_lis_simulator_radiobutton_symbol, "enabled", "selected","LIS Simulator")
        #-LIS Download Mode Order Download Radio Button
        Controls.confirmRadioButton(self,self.lis_downloadmode_order_download_radiobutton_symbol, "enabled", "selected","Order Download")
        #-LIS Download Mode Host-Query Radio Button
        Controls.confirmRadioButton(self,self.lis_downloadmode_host_query_radiobutton_symbol, "enabled", "un-selected","Host-Query")
        #-LIS Historical Lookup checkbox: (checked)
        test.verify(lis_historical_checkbox.enabled == True, "Confirm that the LIS Historical Lookup Checkbox is checked by default")
        #-Purge Pending Orders text field: 999 days
        test.verify(purge_pending_orders.text =="999", "Confirm that the Purge Pending Orders text field contains 999 by default")
        #-Sender ID text field: Bloodhound
        test.verify(sender_id.text == "Bloodhound", "Confirm that the Sender ID text field contains 'Bloodhound'")
        #-Receiver ID text field: LIS
        test.verify(receiver_id.text == "LIS", "Confirm that the Receiver ID text field contain 'LIS'")
        #-Mode Production Radio Button
        Controls.confirmRadioButton(self,self.mode_production_radiobutton_symbol, "enabled", "un-selected","Production")
        #-Mode Training Radio Button
        Controls.confirmRadioButton(self,self.mode_training_radiobutton_symbol, "enabled", "un-selected","Training")
        #-Mode Debug Radio Button
        Controls.confirmRadioButton(self,self.mode_debug_radiobutton_symbol, "enabled", "selected","Debug")
        
    #204. Review the default settings under the LIS ASTM section
    #Confirm each parameters in the LIS ASTM section are defaulted as so: 
    #-Query Wait Time text field: 30000 milliseconds
    #-Message Retry Count text field: 6 
    #-Message Retry Delay text field: 1000 milliseconds
    #-Socket Retry Count text field: 6
    #-Socket Retry Delay text field: 3000 milliseconds
    def confirmLIS_AST_SectionForDefaultControlsAndValues(self):
        #LIS ASTM
        query_wait_time = findObject(self.query_wait_time_textfield_symbol)
        message_retry_count = findObject(self.message_retry_count_textfield_symbol)
        message_retry_delay = findObject(self.message_retry_delay_textfield_symbol)
        socket_retry_count = findObject(self.socket_retry_count_textfield_symbol)
        socket_retry_delay = findObject(self.socket_retry_delay_textfield_symbol)
        
        #-Query Wait Time text field: 30000 milliseconds
        test.verify(query_wait_time.text == "30000", "Confirm that the Query Wait Time Text Field contains 300000")
        #-Message Retry Count text field: 6 
        test.verify(message_retry_count.text == "6", "Confirm that the Message Retry Count Text Field contains 6")
        #-Message Retry Delay text field: 1000 milliseconds
        test.verify(message_retry_delay.text == "1000", "Confirm that the Message Retry Delay Text Field contains 1000")
        #-Socket Retry Count text field: 6
        test.verify(socket_retry_count.text == "6","Confirm that the Socket Retry Count Text Field contains 6")
        #-Socket Retry Delay text field: 3000 milliseconds
        test.verify(socket_retry_delay.text == "3000", "Confirm that the Socket Retry Delay Text Field contains 3000")
    
    #205. Review the default settings under the LIS HL7 section
    #Confirm each parameters in the LIS HL7 section are defaulted as so: 
    #-Reverse AE and AR Meanings checkbox: (checked and disabled)
    #-Retransmit on Receiver Reject checkbox: (checked and disabled)
    #-Retry Count text field: 1
    #-Retry Delay text field: 5000 milliseconds
    def confirmLIS_HL7_SectionForDefaultControlsAndValues(self):
        reverse_ae_and_ar_meanings = findObject(self.reverse_ae_and_ar_meanings_checkbox_symbol)
        retransmit_on_receiver_reject = findObject(self.retransmit_on_receiver_reject_checkbox_symbol)
        retry_count = findObject(self.retry_count_textfield_symbol)
        retry_delay = findObject(self.retry_delay_textfield_symbol)
        
        test.verify(reverse_ae_and_ar_meanings.enabled == False, "Confirm that the Reverse AE and AR Meanings checkbox is not enabled by default")
        test.verify(retransmit_on_receiver_reject.enabled == False, "Confirm that the Retransmit on Receiver Reject checkbox is not enabled by default")
        test.verify(reverse_ae_and_ar_meanings.selected == True, "Confirm that the Reverse AE and AR Meanings checkbox is checked by default")
        test.verify(retransmit_on_receiver_reject.selected == True, "Confirm that the Retransmit on Receiver Reject checkbox is checked by default")
        test.verify(retry_count.enabled == False, "Confirm that the Retry Count Text box is disabled by default")
        test.verify(retry_count.text == "1", "Confirm that the Retry Count text field contains '1'")
        test.verify(retry_delay.enabled == False, "Confirm that the Retry Delay text field is disabled by default")
        test.verify(retry_delay.text == '5000', "Confirm that the Retry Delay text field contains 5000 by default")

    #206. Review the default settings under the LIS TCP/IP Connection section
    #Confirm each parameters in the LIS TCP/IP Connection section are defaulted as so: 
    #-Remote address text field: localhost
    #-Port text field: 3000
    #-Listen on Port text field: 2000
    #-Timeout text field: 60000 milliseconds
    def confirmLIS_TCP_IP_Connection_SectionForDefaultControlsAndValues(self):
        remote_address = findObject(self.remote_address_textfield_symbol)
        port = findObject(self.port_textfield_symbol)
        listen_on_port = findObject(self.listen_on_port_symbol)
        timeout = findObject(self.timeout_textfield_symbol)
                      
        test.verify(remote_address.text == "localhost", "Confirm that the Remote Address text field contains localhost by default")
        test.verify(port.text == "3000", "Confirm that the Port text field contains 3000 by default")
        test.verify(listen_on_port.text == "2000", "Confirm that the Listen on Port contains 2000 by default")
        test.verify(timeout.text == "60000", "Confirm that the Timeout text field contains 60000 by default")
