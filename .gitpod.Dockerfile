FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN bash -lc "gem install jekyll bundler"
