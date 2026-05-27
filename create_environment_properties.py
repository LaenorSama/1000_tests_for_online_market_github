import platform
import os
from pathlib import Path

# Путь к папке allure-results берём из переменной окружения
allure_results_dir = os.getenv("ALLURE_RESULTS", "allure-results")

# Остальные данные для отчета
#browser = os.getenv("BROWSER", "Chrome")
#os_name = os.getenv("OS", platform.system())
#branch = os.getenv("BRANCH", "unknown")
commit = os.getenv("GITHUB_SHA", "unknown")
build_number = os.getenv("GITHUB_RUN_NUMBER", "0")
python_version = platform.python_version()
#job_run_id = os.getenv("ALLURE_JOB_RUN_ID", "")

# Определяем реальную ОС runner-а
os_info = f"{platform.system()} {platform.release()} ({platform.version()})"

# Создаем файл environment.properties
env_file = Path(allure_results_dir) / "environment.properties"
env_file.parent.mkdir(parents=True, exist_ok=True)

with open(env_file, "w") as f:
    #f.write(f"OS={os_name}\n")
    f.write(f"Python_version={platform.python_version()}\n")
    #f.write(f"Browser={browser}\n")
    #f.write(f"Branch={branch}\n")
    f.write(f"Commit={commit}\n")
    f.write(f"Build_number={build_number}\n")
    #f.write(f"Job_run_id={job_run_id}\n")
    f.write(f"Worker_OS={os_info}\n")

print(f"Environment properties written to {env_file}")
