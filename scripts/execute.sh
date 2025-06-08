for f in ../apis/*.yaml; do
  filename="${f##*/}"
  name_no_ext="${filename%.yaml}"
  npx @redocly/cli build-docs "$f" -o "../apis/html/${name_no_ext}.html"
done