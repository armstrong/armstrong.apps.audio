from datetime import datetime 
import random

from ..models import Audio
from armstrong.core.arm_content.tests import load_audio_model


def load_audio_pub(filename):
    model_args = dict(pub_date=datetime.now(),
                pub_status='P',
                slug='random-slug-%s' % random.randint(100, 1000),
                title='Random title %s' % random.randint(100, 1000),
                )

    am = load_audio_model(filename=filename,
                     file_field_name='file',
                     model=Audio,
                     model_args=model_args)
    return am


