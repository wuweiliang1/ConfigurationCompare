import sys
import copy


def compare(prefix_key, raw_config1, raw_config2):
    with open(raw_config1) as fd1, open(raw_config2) as fd2:
        configuration1 = {prefix_key: {}}
        configuration2 = {prefix_key: {}}
        # Find all the configuration start with matching key and load them into list
        for line in fd1:
            if line.startswith(prefix_key):
                configuration1[prefix_key][line] = False

        for line in fd2:
            if line.startswith(prefix_key):
                configuration2[prefix_key][line] = False
    # Simple comparison
    for configurationline in configuration1[prefix_key]:
        if configurationline in configuration2[prefix_key]:
            configuration2[prefix_key][configurationline] = True
            configuration1[prefix_key][configurationline] = True
    different_config1 = copy.deepcopy(configuration1)
    different_config2 = copy.deepcopy(configuration2)
    # Remove all duplicate configuration
    for configurationline in configuration1[prefix_key]:
        if configuration1[prefix_key][configurationline]:
            del different_config1[prefix_key][configurationline]

    for configurationline in configuration2[prefix_key]:
        if configurationline in configuration1[prefix_key] and configuration1[prefix_key][configurationline]:
            del different_config2[prefix_key][configurationline]

    return different_config1, different_config2


def main():
    if len(sys.argv) != 3:
        print('you should provide two argument for running this script')
        exit(-1)
    keys = ['add lb vserver ', 'add serviceGroup', 'add server', 'bind serviceGroup']
    for key in keys:
        different1, different2 = compare(key, sys.argv[1], sys.argv[2])
        print('=============%s %s Configuration==============' % (sys.argv[1], key))
        for mykey in different1[key].keys():
            print(mykey)
        print('=============%s %s Configuration==============' % (sys.argv[2], key))
        for mykey in different2[key].keys():
            print(mykey)

main()
