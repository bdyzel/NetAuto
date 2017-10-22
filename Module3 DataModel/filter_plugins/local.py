import re

class FilterModule(object):
  def to_site_wildcard(self, address):
    return re.sub(r'^((?:[0-9]{1,3}\.){3})\d+$', r'\1', address)

  def filters(self):
    return {
      'to_site_wildcard': self.to_site_wildcard,
    }
