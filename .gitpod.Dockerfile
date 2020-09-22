FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN bash -lc "gem install jekyll bundler rake jekyll-mermaid public_suffix -v 4.0.5 concurrent-ruby -v 1.1.6 rexml -v 3.2.4 rouge -v 3.21.0 jekyll-paginate -v 1.1.0"
