import json 
import os 
import subprocess 
from pywps import Process, ComplexInput, LiteralOutput, Format 
from pywps.wpsserver import temp_dir 

class TotalLength(Process): 
    """Process calculating length of given polygon
    """ 
    def __init__(self): 
        
        inputs = [ComplexInput('layer', 'Layer', [Format('application/gml+xml')])] 
        
        outputs = [LiteralOutput('length', 'Total length', data_type='string')] 
        
        
        super(TotalLength, self).__init__(
            self._handler, 
            identifier='grass_length', 
            title='Total line length', 
            abstract="""Process returns the length of each
            feature from a submitted GML file""", 
            inputs=inputs, 
            outputs=outputs, 
            store_supported=True, 
            status_supported=True, 
            grass_location="epsg:3358") 
        
        def _handler(self, request, response):  
            # ogr2ogr requires gdal-bin 
            
            from grass.script import core as grass
             
            grass.run_command("v.in.ogr", input=request.inputs["layer"][0].file, output="lines") 
            output = grass.pipe_command("v.report", map="lines", option="length") 
            line_length = 0 
            
            for line in output.stdout.readlines()[1:]: 
                line = line.strip() 
                length = line.split("|")[-1] 
                line_length += float(length) 
            
            response.outputs['length'].data = line_length 
            return response
