import os
from typing import Optional

import fire
from metagpt.logs import logger
from metagpt.roles.di.engineer2 import Engineer2
from metagpt.tools.libs.cr import CodeReview


def read_code_from_file(file_path: str) -> Optional[str]:
    """
    Read code content from a file.

    Args:
        file_path: Path to the file containing code to review

    Returns:
        str: Content of the file if successful, None if file cannot be read

    Raises:
        FileNotFoundError: If the specified file does not exist
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None


async def main(file_path: str):
    """
    Main function that reads code from a file and performs code review.

    Args:
        file_path: Path to the file containing code to review
    """
    # Read code from file
    code_content = read_code_from_file(file_path)
    if code_content is None:
        return
    logger.info(code_content)
    # Initialize Engineer2 role and CodeReview
    role = Engineer2(tools=["Plan", "Editor:write,read", "RoleZero", "ValidateAndRewriteCode", "CodeReview"])
    cr = CodeReview()
    role.tool_execution_map.update({"CodeReview.review": cr.review, "CodeReview.fix": cr.fix})

    # Run code review on the file content
    await role.run("if not os.path.exists(file_path):")


if __name__ == "__main__":
    fire.Fire(main)
