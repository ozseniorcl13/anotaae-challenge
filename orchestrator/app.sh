#!/bin/bash

usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -e          Set environment (default: dev)"
    echo "  -op         Define operation to be performed (Up and Down)"
    echo "  -b          Build before running"
}

run () {

    # Get arguments
    p_build=""

    while [[ $# -gt 0 ]]; do
        key="$1"
        case $key in
        -e | --environment)
            p_environment="$2" && shift 2
            ;;
        -op | --operation)
            p_operation="$2" && shift 2
            ;;
        -b | --build)
            p_build="--build" && shift 1
            ;;
        *)
            usage && exit 1
            ;;
        esac
    done
    
    p_environment=${p_environment:="dev"}
    p_operation=${p_operation:='up'}

    docker compose -p catalog-$p_environment --env-file env/.$p_environment.env $p_operation $p_build --remove-orphans

}

run $@
