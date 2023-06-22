'''
LOGGING:

Rastrea los eventos que ocurren cuando se ejecuta algún software. 
Las funciones de registro se denominan según el nivel o la gravedad de los eventos que se utilizan para rastrear. 

DEBUG (logging.info() o logging.debug()): Información detallada, típicamente de interés sólo durante el diagnóstico de problemas.
INFO (print()): Confirmación de que las cosas están funcionando como se esperaba.
WARNING (warnings.warn()): Un indicio de que algo inesperado sucedió, o indicativo de algún problema en el futuro cercano (por ejemplo, 
«espacio de disco bajo»). El software sigue funcionando como se esperaba.
ERROR (logging.error()): Debido a un problema más grave, el software no ha sido capaz de realizar alguna función.
CRITICIAL (logging.critical() ): Un grave error, que indica que el programa en sí mismo puede ser incapaz de seguir funcionando.


El nivel por defecto es WARNING, lo que significa que sólo los eventos de este nivel y superiores serán rastreados, a menos que 
el paquete de registro esté configurado para hacer lo contrario.

'''
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')