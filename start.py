import os
import subprocess
from loguru import logger
from typing import List, Union, Iterable, Any

def read_from_file(filepath: str) -> Union[Iterable[str], None]:
    try:
        with open(filepath, 'r', encoding="utf-8") as fp:
            return [line.strip() for line in fp]
    except FileExistsError:
        logger.error("文件不存在")
    except Exception as e:
        logger.error(f"文件读取错误: {str(e)}")


# def command_argv(type: str, source: str, id: str) -> str:
#     return rf"""
#     java -cp mc-component-automation-tool.jar tech.arikin.automation.image.ImageApiApplication D D:\brand_images\{source}_source {source} {type} {id}
#     """.strip().replace(" <built-in function id>", "")


def start():
    ids: Any = read_from_file(r"ids.txt")
    try:

        # java_library_path = "/opt/homebrew/Cellar/webp/1.5.0/lib"
        # logger.debug(command_argv("B", "burberry", "2c9fbd59970a3496019754292a8c66e0"))
        # subprocess.run(["dir"])
        # 执行命令并捕获输出
        for index, idx in enumerate(ids, start=1):
            # logger.debug(command_argv("B", "BURBERRY", id).split(" "))
            logger.debug(f"正在处理第{index}个: {idx}")
            # os.system(command_argv("B", "Celine", idx))
            # os.system(command_argv("Q", "Celine", idx))
            # os.system(rf'java  -cp mc-component-automation-tool.jar tech.arikin.automation.image.ImageApiApplication D ./celine "CELINE" B {idx}')
            # os.system(rf'java -cp mc-component-automation-tool.jar tech.arikin.automation.image.ImageApiApplication D D:\brand_images\CELINE_source "CELINE" Q {idx}')
            command = [
                "java",
                "-cp",
                "mc-component-automation-tool.jar",
                "tech.arikin.automation.image.ImageApiApplication",
                "D",
                "./celine",
                "CELINE",
                "B",
                idx
            ]
            subprocess.run(command)

    except Exception as e:
        logger.error(f"图片处理错误: {str(e)}")

        # subprocess.run(['dir'])
        # subprocess.run(["java -cp mc-component-automation-tool.jar tech.arikin.automation.image.ImageApiApplication D",
        #                 r"D:\brand_images\burberry_source", "BURBERRY", "Q", id])
        # subprocess.run(command_argv("B", "BURBERRY", id).split(" "))
        # subprocess.run(command_argv("Q", "BURBERRY", id).split(" "))


if __name__ == '__main__':
    start()
