name: CI/CD Pipeline for MySQL Database Deployment

on:
  push:
    branches:
      - main  # Trigger the workflow on push to the main branch

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install mysql-connector-python

    - name: Run SQL Script
      env:
        MYSQL_HOST: ${{ secrets.MYSQL_HOST }}      # Azure MySQL host
        MYSQL_USER: ${{ secrets.MYSQL_USER }}      # MySQL Username (e.g., mysqladmin)
        MYSQL_PASSWORD: ${{ secrets.MYSQL_PASSWORD }}  # MySQL 
