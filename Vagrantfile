Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |v| 
    v.memory = 512
    v.cpus = 1
    v.gui = false
  end

  config.vm.network :forwarded_port, guest: 8000, host: 8000

  # Enable provisioning with a shell script.
  config.vm.provision :shell, path: "vagrant_setup.sh"

end
