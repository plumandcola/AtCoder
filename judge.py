import requests, re, subprocess

# 幅
COL_WIDTH = 40

# パディング関数
def pad(s):
    if len(s) < COL_WIDTH:
        return s + " " * (COL_WIDTH - len(s))
    return s[:COL_WIDTH]

# ANSI colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

link = "" #ここに、AtCoderの問題が載っているURLを入れる
python_path = "main.py" #ここに、コードを書いたPythonファイルへのパスを入れる

res = requests.get(link)
#print(res.text)

for i in range(1, 10):
    found = re.search(rf"入力例 {i}(.*?)</pre>", res.text, re.DOTALL)
    if found is None:
        break

    input_i = re.sub("\r\n", "\n", found.group(1))
    input_i = re.sub("<.+?>", "", input_i) #HTMLタグを除去
    input_i = input_i.lstrip() #昔のは、入出力例の最初に無駄な改行が入るため、それを除去

    print(f"\n=== Sample Input {i} ===")
    print(input_i)

    result = subprocess.run(
        ["python3", python_path],
        input=input_i,
        text=True,
        capture_output=True
        )
    
    stdout = result.stdout
    stderr = result.stderr

    if result.returncode != 0:
        print(f"{RED}Runtime Error (exit code {result.returncode}){RESET}")
        print("\n--- 標準エラー出力 ---")
        print(f"{RED}{stderr.strip()}{RESET}")
        print("\n--- 標準出力 ---")
        print(stdout.strip())
        continue

    output_i = re.search(rf"出力例 {i}(.*?)</pre>", res.text, re.DOTALL).group(1)
    output_i = re.sub("<.+?>", "", output_i) #HTMLタグを除去
    output_i = output_i.lstrip() #昔のは、入出力例の最初に無駄な改行が入るため、それを除去

    # 行に分割
    expected_lines = output_i.split("\r\n")
    result_lines = stdout.split("\n")

    #print(stdout)

    # 行数を揃える
    max_len = max(len(expected_lines), len(result_lines))
    expected_lines += [""] * (max_len - len(expected_lines))
    result_lines += [""] * (max_len - len(result_lines))

    # ヘッダー
    print("   ", "|", f"Expected Output {i}".ljust(COL_WIDTH), "|", f"Your Output {i}")
    print("---", "+", "-" * COL_WIDTH, "+", "-" * COL_WIDTH)

    # 行ごとに比較して表示
    for j in range(max_len):
        e_pad = pad(expected_lines[j])
        r_pad = pad(result_lines[j])

        if expected_lines[j] == result_lines[j]:
            # 同じ行は緑
            print(f"{j+1:3} | {GREEN}{e_pad}{RESET} | {GREEN}{r_pad}{RESET}")
            #continue #出力の行数が多い時は、printの部分をコメントアウトし、代わりにcontinue
        else:
            # 異なる行は赤
            print(f"{j+1:3} | {RED}{e_pad}{RESET} | {RED}{r_pad}{RESET}")
