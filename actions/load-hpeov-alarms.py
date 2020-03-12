# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import DwrAlarmsBaseAction


class loadDb(DwrAlarmsBaseAction):
    def run(self, alarms):

        mydb = self.client["app_db"]
        known = mydb["dwralarms"]

        new_alarm={}

        for alarm in alarms:
            new_alarm['vendor']='hpe-oneview'
            myquery = { "u_uuid" : alarm['resourceUri'] }
            records = known.find(myquery).count()
            if records == 0:
                new_alarm['u_sev']=alarm['severity']
                new_alarm['u_desc']=alarm['description']
                new_alarm['u_uuid']=alarm['resourceUri']
                write_record = known.insert_one(new_alarm)
                # write_record = process.insert_one(alarm)
        return (records)
