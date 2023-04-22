## nameを呼び出し元の値にしたい。


import logging

# loggerを定義
logger = logging.getLogger(__name__)

def setting(logfilename):
    # loggerのログレベルを設定
    logger.setLevel(logging.INFO)
    # loggerのフォーマット、出力先ファイルを定義
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)-8s:%(name)s - %(message)s')
    file_handler = logging.FileHandler(logfilename + '.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)    
    file_handler.setFormatter(formatter)
    # コンソールに出力するためのStreamHandlerを設定
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # loggerにそれぞれのハンドラーを追加
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

def debug(log):
    logger.debug(log)

def info(log):
    logger.info(log)

def warning(log):
    logger.warning(log)

def error(log):
    logger.error(log, exc_info=True)

def critical(log):
    logger.critical(log, exc_info=True)
