FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN bash -lc "gem install jekyll bundler rake jekyll-mermaid public_suffix:4.0.5 concurrent-ruby:1.1.6 rexml:3.2.4 rouge:3.21.0 jekyll-paginate:1.1.0"
