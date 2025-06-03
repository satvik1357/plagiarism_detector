import os
import itertools
from flask import Flask, render_template, request
from utils.processor_text import extract_text, calculate_text_similarity
from utils.processor_code import calculate_code_similarity, is_code_file, is_text_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files')

        if len(uploaded_files) < 2:
            return render_template('index.html', error="Please upload at least two files.")

        try:
            group_size_input = request.form.get('group_size', '').strip()
            group_size = int(group_size_input) if group_size_input else None
        except ValueError:
            group_size = None

        file_paths = []
        filetypes = []

        for f in uploaded_files:
            if f.filename == '':
                continue
            filename = 'file_' + f.filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(path)
            file_paths.append(path)
            if is_code_file(f.filename):
                filetypes.append('code')
            elif is_text_file(f.filename):
                filetypes.append('text')
            else:
                filetypes.append('unknown')

        if len(set(filetypes)) > 1 or 'unknown' in filetypes:
            for path in file_paths:
                os.remove(path)
            return render_template('index.html', error="All uploaded files must be of the same supported type.")

        filetype = filetypes[0]
        group_results = []
        pairwise_results = []
        show_group_results = False

        # Group-wise similarity (only if group_size is provided and valid)
        if group_size and group_size >= 2 and group_size <= len(file_paths):
            for combo in itertools.combinations(file_paths, group_size):
                names = [os.path.basename(f) for f in combo]

                if filetype == 'code':
                    scores = [calculate_code_similarity(f1, f2) for f1, f2 in itertools.combinations(combo, 2)]
                else:
                    texts = [extract_text(f) for f in combo]
                    scores = [calculate_text_similarity(texts[i], texts[j])
                              for i in range(len(texts)) for j in range(i + 1, len(texts))]

                avg_score = round(sum(scores) / len(scores), 2) if scores else 0.0
                group_results.append({'files': names, 'score': avg_score})

            show_group_results = True

        # Overall similarity for all files together
        all_files_names = [os.path.basename(f) for f in file_paths]

        if filetype == 'code':
            all_scores = [calculate_code_similarity(f1, f2) for f1, f2 in itertools.combinations(file_paths, 2)]
        else:
            all_texts = [extract_text(f) for f in file_paths]
            all_scores = [calculate_text_similarity(all_texts[i], all_texts[j])
                          for i in range(len(all_texts)) for j in range(i + 1, len(all_texts))]

        all_avg_score = round(sum(all_scores) / len(all_scores), 2) if all_scores else 0.0

        for path in file_paths:
            os.remove(path)

        return render_template(
            'result.html',
            pairwise_results=pairwise_results,
            group_results=group_results,
            group_size=group_size,
            all_files_names=all_files_names,
            all_avg_score=all_avg_score,
            filetype=filetype,
            show_group_results=show_group_results
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
