# -*- coding:utf-8 -*-

import sys
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
reload(sys)
sys.path.append("../")
from global_utils import es_sensor as es
from global_utils import index_manage_sensing, type_manage_sensing, id_sensing_task, index_content_sensing, type_content_sensing, index_monitor_task, type_monitor_task

def mappings_manage_sensing_task():
    index_info = {
        'settings':{
                'number_of_replicas': 0,
                'number_of_shards': 5,
                'analysis':{
                    'analyzer':{
                        'my_analyzer':{
                            'type': 'pattern',
                            'pattern': '&'
                        }
                    }
                }
            },
        "mappings":{
            "task":{
                "properties":{
                    "task_name":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "task_type":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "last_time":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "create_by":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "processing_status":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "stop_time":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "remark":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "social_sensors":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "history_status":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "create_at":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "warning_status":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "finish":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "burst_reason":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    'xnr_user_no':{     # 增加虚拟人
                        'type':'string',
                        'index':'not_analyzed'
                    }
                }
            }
        }
    }
    exist_indice = es.indices.exists(index=index_manage_sensing)
    if not exist_indice:
        es.indices.create(index=index_manage_sensing, body=index_info, ignore=400)

def mappings_social_sensing_text():
    index_info = {
        'settings':{
                'number_of_replicas': 0,
                'number_of_shards': 5,
                'analysis':{
                    'analyzer':{
                        'my_analyzer':{
                            'type': 'pattern',
                            'pattern': '&'
                        }
                    }
                }
            },
        "mappings":{
            "text":{
                "properties":{
                    "trendline":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "duplicate":{
                        "type": "float",
                        "index": "not_analyzed"
                    },
                    "uid_prediction":{
                        "type": "float",
                        "index": "not_analyzed"
                    },
                    "weibo_prediction":{
                        "type": "float",
                        "index":"not_analyzed"
                    },
                    "mid_topic_value":{
                        "type": "float",
                    },
                    "detect_ts":{
                        "type": "long",
                    },
                    "text":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "sensitive_words_string":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "sensitive":{
                        "type": "float",
                    },
                    "uid":{
                        "type": "string",
                    },
                    "user_fansnum":{
                        "type": "long"
                    },
                    "mid":{
                        "type": "string"
                    },
                    "keyswords_string":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "geo":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "ip":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "timestamp":{
                        "type": "long"
                    },
                    "message_type":{
                        "type": "long"
                    },
                    "type":{
                        "type": "long"
                    },
                    'topic_field':{
                        'type':'string',
                        'index':'not_analyzed'
                    },
                    'compute_status':{   # 0- 尚未计算， 1-正在计算，2- 计算王成
                        'type':'long'
                    },
                    'xnr_user_no':{    # 增加虚拟人
                        'type':'string',
                        'index':'not_analyzed'
                    }
                }
            }
        }
    }
    exist_indice = es.indices.exists(index=index_content_sensing)
    if not exist_indice:
        es.indices.create(index=index_content_sensing, body=index_info, ignore=400)

def mappings_monitor_task():
    index_info = {
        'settings':{
                'number_of_replicas': 0,
                'number_of_shards': 5,
                'analysis':{
                    'analyzer':{
                        'my_analyzer':{
                            'type': 'pattern',
                            'pattern': '&'
                        }
                    }
                }
            },
        "mappings":{
            "task":{
                "properties":{
                    "task_name":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "from_date":{
                        "type": "long",
                    },
                    "to_date":{
                        "type": "long",
                    },
                    "create_user":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "processing_status":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "event_detail":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "delete":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "create_at":{
                        "type": "long",
                    },
                    "event_category":{
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "keywords":{
                        "type": "string",
                        "index": "not_analyzed"
                    }
                }
            }
        }
    }
    exist_indice = es.indices.exists(index=index_monitor_task)
    if not exist_indice:
        es.indices.create(index=index_monitor_task, body=index_info, ignore=400)

if __name__ == "__main__":
    mappings_manage_sensing_task()
    mappings_monitor_task()
    mappings_social_sensing_text()


