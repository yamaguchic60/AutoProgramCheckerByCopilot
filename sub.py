import subprocess

def run_script_and_monitor_output(script_name):
    process = subprocess.Popen(
        ["python", script_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        universal_newlines=True
    )

    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())
        elif process.poll() is not None:
            break

    # 標準エラーも読み込む
    stderr = process.stderr.read()
    if stderr:
        print(stderr.strip())

    return process.returncode

def main():
    # test.pyの処理を実行し、出力を監視
    return_code = run_script_and_monitor_output("test.py")
    #print(f"test.py finished with return code {return_code}")

    # test.pyの終了後にobservetest.pyを実行
    #print("Running dev.py...")
    run_script_and_monitor_output("dev.py")

if __name__ == "__main__":
    main()
