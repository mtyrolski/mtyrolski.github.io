# Base image: Ruby with necessary dependencies for Jekyll
FROM ruby:3.2

ENV BUNDLE_PATH=/usr/local/bundle \
    BUNDLE_APP_CONFIG=/usr/local/bundle

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy dependency manifests before the source so this layer remains cacheable.
COPY Gemfile Gemfile.lock ./

# Install bundler and dependencies
RUN gem install bundler:2.4.19 && bundle install

# Command to serve the Jekyll site
CMD ["bundle", "exec", "jekyll", "serve", "-H", "0.0.0.0", "-w", "--config", "_config.yml,_config_docker.yml"]
