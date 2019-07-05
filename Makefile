
export PLOTLY_RENDERER=notebook_connected

MD_DIR ?= notebooks
IPYNB_DIR ?= build/ipynb
HTML_DIR ?= build/html
FAIL_DIR ?= build/failures
MD_FILES := $(shell grep -l v4upgrade $(MD_DIR)/*)
IPYNB_FILES := $(patsubst $(MD_DIR)/%.md,$(IPYNB_DIR)/%.ipynb,$(MD_FILES))
HTML_FILES := $(patsubst $(MD_DIR)/%.md,$(HTML_DIR)/2019-07-03-%.html,$(MD_FILES))

all: $(HTML_FILES)

.PRECIOUS: $(IPYNB_FILES)

$(IPYNB_DIR)/%.ipynb: $(MD_DIR)/%.md
	@mkdir -p $(IPYNB_DIR)
	@echo "[jupytext]  $<"
	@jupytext $< --to notebook --quiet --output $@

$(HTML_DIR)/2019-07-03-%.html: $(IPYNB_DIR)/%.ipynb
	@mkdir -p $(HTML_DIR)
	@mkdir -p $(FAIL_DIR)
	@echo "[nbconvert] $<"
	@touch $@ && grep -q `shasum $<` $@ || \
		jupyter nbconvert $< --to html --template nb.tpl \
	  	--output-dir $(HTML_DIR) --output 2019-07-03-$*.html \
	  	--execute > $(FAIL_DIR)/$* 2>&1  \
		&& rm -f $(FAIL_DIR)/$* \
		&& echo "" >> $@ \
		&& echo \<\!-- `shasum $<` --\> >> $@

