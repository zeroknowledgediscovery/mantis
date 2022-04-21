"""
Detecting emergent anomlaies in data streams without
prior specification of templates of anomalous
dynamics. Uses Probabilistic Finite Automata
moels to infer classes of normal behaviors, and
emergent anomalies.


Installation:
   ```
      pip install patternly
   ```
   or
   ```
      pip3 install patternly --user
   ```
"""
from patternly._utils import RANDOM_NAME, os_remove
from patternly.detection import AnomalyDetection, StreamingDetection, ContinuousStreamingDetection
