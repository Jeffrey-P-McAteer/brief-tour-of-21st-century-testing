
# CSharp .net core example

## Creating test project

```bash
dotnet new console

# Modify Program.cs

# Create Tests.cs

# Update csharp_net_core.csproj to include XUnit references

```

## Compile and run project (manual testing)

```bash
dotnet build

dotnet run -- 1 2 3 4 5 6 7 8

```

## Run tests (automated testing + reports & metrics)

```bash

# Install report generation utility and set environment so tool can find itself
dotnet tool install --global minicover
export PATH="$PATH:$HOME/.dotnet/tools"
export DOTNET_ROOT=$(dirname $(which dotnet))

# generate .dll files
dotnet test

# Instrument .dll files
minicover instrument --sources '**/*.cs' --tests '**/*.cs'

# Execute test, using instrumented .dll files
dotnet test --no-build

# Generate report
minicover htmlreport

# Read report
open coverage-html/index.html

```
