# Copyright 2011 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import db

class DBStub(object):
  def __init__(self, settings):
    self.db = db.DB(settings)

  def on_bound_to_server(self, server):
    server.add_json_route('/dirs/new', self.new_dir, ['POST'])
    server.add_json_route('/dirs', self.dirs, ['GET'])
    server.add_json_route('/dirs/(\d+)', self.dirN, ['GET','DELETE'])
    server.add_json_route('/search', self.search, ['POST'])

  def dirN(self, req, verb, data):
    pass

  def dirs(self, req, verb, data):
    pass

  def new_dir(self, req, verb, data):
    pass

  def search(self,query):
    return