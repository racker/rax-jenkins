from fabric.api import sudo, hide, run, env


def execute(node):
    """
    Removes the opscode repo
    Sets up the otter repo
    Installs omnibus Chef
    """

    env.linewise = True
    with hide('everything'):
        url = "http://packages.as.rax.io"
        codename = run('lsb_release -cs')
        content = "deb {0} {1} main".format(url, codename)
        chef_binaries = ['chef-client', 'chef-solo', 'knife', 'ohai', 'shef']
        for binary in chef_binaries:
            sudo('rm -f /usr/local/bin/{0}'.format(binary))
        sudo('rm -f /etc/apt/sources.list.d/opscode.list')
        sudo('echo "{0}" > /etc/apt/sources.list.d/otter.list'.format(content))
        sudo('curl {0}/cache/pubkey.gpg | apt-key add -'.format(url))
        sudo('apt-get update')
    sudo('apt-get install chef')
    sudo('apt-get -y autoremove')
