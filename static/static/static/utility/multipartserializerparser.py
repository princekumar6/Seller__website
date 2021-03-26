from json import loads

from rest_framework import parsers


class NestedMultipartParser(parsers.MultiPartParser):
    """
    Parser join the files into object which was sended separately
    """
    result=None
    
    def replacer(self,obj):
        objtype=type(obj)
        if objtype==dict:
            for x in obj:
                xtype=type(obj[x])
                if xtype==dict:
                    self.replacer(obj)
                elif xtype==list:
                    for y in obj[x]:
                        if type(y)==dict or type(y)==list:
                            self.replacer(y)
                elif xtype==str:
                    if obj[x].startswith('file_id_'):
                        if obj[x] in self.result.files:
                            temp=self.result.files[obj[x]]
                            obj[x]=self.result.files[obj[x]]
                            del temp

    def parse(self, stream, media_type=None, parser_context=None):
        self.result= super().parse(stream=stream, media_type=media_type, parser_context=parser_context)
        data=loads(self.result.data['json'])
        self.replacer(data)        
        return data
