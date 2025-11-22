import os
from datetime import datetime

def patch_runtime_lavamoat(base_path):
    target_filename = "runtime-lavamoat.js"
    search_text = 'scuttleGlobalThis":{"enabled":true'
    replace_text = 'scuttleGlobalThis":{"enabled":false'
    log_entries = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == target_filename:
                full_path = os.path.normpath(os.path.join(root, file))
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    if search_text in content:
                        content = content.replace(search_text, replace_text)
                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        msg = f"✅ Đã sửa file: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                    else:
                        msg = f"⚠️ Không tìm thấy chuỗi trong: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                except Exception as e:
                    msg = f"❌ Lỗi với file {full_path}: {e}"
