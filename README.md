# github-commit-harvester

## Prepare usage

```
pipenv install
pipenv shell
```

## Usage

```python3 main.py
2024-01-28 20:44:17 | INFO     | Cloning osism/openstack-themes
2024-01-28 20:44:18 | INFO     | Cloning osism/openstack-octavia-amphora-image
2024-01-28 20:44:18 | INFO     | Cloning osism/openstack-project-manager
2024-01-28 20:44:23 | INFO     | Cloning osism/osism.github.io
2024-01-28 20:44:24 | INFO     | Cloning osism/python-osism
2024-01-28 20:44:24 | INFO     | Cloning osism/container-image-inventory-reconciler
2024-01-28 20:44:25 | INFO     | Cloning osism/release
2024-01-28 20:44:26 | INFO     | Cloning osism/sbom
2024-01-28 20:44:27 | INFO     | Cloning osism/cloud-in-a-box
2024-01-28 20:44:27 | INFO     | Cloning osism/openstack-resource-manager
2024-01-28 20:44:28 | INFO     | Cloning osism/ansible-collection-validations
2024-01-28 20:44:29 | INFO     | Cloning osism/openstack-simple-stress
2024-01-28 20:44:29 | INFO     | Cloning osism/deb-packaging
2024-01-28 20:44:30 | INFO     | Cloning osism/node-image
2024-01-28 20:44:31 | INFO     | Cloning osism/cfg-cookiecutter
2024-01-28 20:44:31 | INFO     | Cloning osism/openstack-sandbox-manager
2024-01-28 20:44:32 | INFO     | Cloning osism/ansible-playbooks-manager
2024-01-28 20:44:33 | INFO     | Cloning osism/testbed
2024-01-28 20:44:34 | INFO     | Cloning osism/kolla-operations
2024-01-28 20:44:35 | INFO     | Cloning osism/container-images-kolla
2024-01-28 20:44:37 | INFO     | Cloning osism/ansible-collection-commons
2024-01-28 20:44:38 | INFO     | Cloning osism/ci-image
2024-01-28 20:44:38 | INFO     | Cloning osism/defaults
2024-01-28 20:44:39 | INFO     | Cloning osism/ansible-playbooks
2024-01-28 20:44:39 | INFO     | Cloning osism/container-image-osism-ansible
2024-01-28 20:44:40 | INFO     | Cloning osism/cfg-generics
2024-01-28 20:44:41 | INFO     | Cloning osism/terraform-base
2024-01-28 20:44:42 | INFO     | Cloning osism/container-images
2024-01-28 20:44:42 | INFO     | Cloning osism/container-image-ceph-ansible
2024-01-28 20:44:43 | INFO     | Cloning osism/k8s-capi-images
2024-01-28 20:44:44 | INFO     | Cloning osism/ansible-collection-services
2024-01-28 20:44:45 | INFO     | Cloning osism/container-image-kolla-ansible
2024-01-28 20:44:46 | INFO     | Cloning osism/openstack-image-manager
2024-01-28 20:44:46 | INFO     | Cloning osism/openstack-flavor-manager
2024-01-28 20:44:47 | INFO     | Cloning osism/tests
2024-01-28 20:44:47 | INFO     | Processing 2023-12-01 00:00:00
ceph: remove interface parameters (#552), https://github.com/osism/cfg-cookiecutter/commit/e4f5a780b30f0a87931c315bed6ba3e7061e3cb9
2024-01-28 20:44:47 | INFO     | Processing 2023-12-02 00:00:00
2024-01-28 20:44:47 | INFO     | Processing 2023-12-03 00:00:00
Print a note when a task output timed out (#716), https://github.com/osism/python-osism/commit/f4e1ba9db3f253ff5c69385eaabe218eb53c4b6d
Inform that there may be a short delay (#717), https://github.com/osism/python-osism/commit/8871a58e8c059bc9afc9a0c0b959c3405eed85d1
2024-01-28 20:44:48 | INFO     | Processing 2023-12-04 00:00:00
2023.2: disable some openstack images for the moment, https://github.com/osism/release/commit/0e60128c1d18010c60cd10f6e3bc343676981f57
Use ansible strategy free by default everywhere (#338), https://github.com/osism/ansible-playbooks/commit/1c9df625097d71025ad944df1503ec7370f0f7b6
Remove json_stats ansible module (#462), https://github.com/osism/container-image-osism-ansible/commit/83380f5af75f1a865c76f862304d6170f3b08357
[...]
```

### Sample output

| Date       | Title                                                                          | URL                                                                                                    |
|------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| 2023-12-01 |                                                                                |                                                                                                        |
|            | ceph: remove interface parameters (#552)                                       | https://github.com/osism/cfg-cookiecutter/commit/e4f5a780b30f0a87931c315bed6ba3e7061e3cb9              |
| 2023-12-02 |                                                                                |                                                                                                        |
| 2023-12-03 |                                                                                |                                                                                                        |
|            | Print a note when a task output timed out (#716)                               | https://github.com/osism/python-osism/commit/f4e1ba9db3f253ff5c69385eaabe218eb53c4b6d                  |
|            | Inform that there may be a short delay (#717)                                  | https://github.com/osism/python-osism/commit/8871a58e8c059bc9afc9a0c0b959c3405eed85d1                  |
| 2023-12-04 |                                                                                |                                                                                                        |
|            | 2023.2: disable some openstack images for the moment                           | https://github.com/osism/release/commit/0e60128c1d18010c60cd10f6e3bc343676981f57                       |
|            | Use ansible strategy free by default everywhere (#338)                         | https://github.com/osism/ansible-playbooks/commit/1c9df625097d71025ad944df1503ec7370f0f7b6             |
|            | Remove json_stats ansible module (#462)                                        | https://github.com/osism/container-image-osism-ansible/commit/83380f5af75f1a865c76f862304d6170f3b08357 |
|            | Use osism.github.io as docs URL (#463)                                         | https://github.com/osism/container-image-osism-ansible/commit/32a0a8efdedcd9a632b942f23a9a8095a5938ca9 |
|            | Remove ara-wrapper (#464)                                                      | https://github.com/osism/container-image-osism-ansible/commit/4129fa2abcc0a2b439cfdc507e9f5d85ae2d872e |
|            | zuul: add python-black job (#465)                                              | https://github.com/osism/container-image-osism-ansible/commit/65aa1f41177421bb8a4a17e22129ecdb87a2a5b3 |
|            | Remove json_stats ansible module (#409)                                        | https://github.com/osism/container-image-ceph-ansible/commit/e03ce0b73c6725a6997c704518c689d37729dc57  |
|            | Remove ara-wrapper (#410)                                                      | https://github.com/osism/container-image-ceph-ansible/commit/80a69efd56d8df69e1e1293ae55e1b190bed184f  |
|            | zuul: add python-black job (#411)                                              | https://github.com/osism/container-image-ceph-ansible/commit/47555b7bc1a5fa7ffa7c27b01f87ab6353f54f11  |
|            | Remove json_stats ansible module (#550)                                        | https://github.com/osism/container-image-kolla-ansible/commit/274e2980aca7a771ecaff7430916d27de2d7a797 |
|            | Remove ara-wrapper (#551)                                                      | https://github.com/osism/container-image-kolla-ansible/commit/a4e53011529d8f97758afa4afdf198e196518434 |
|            | zuul: add python-black job (#552)                                              | https://github.com/osism/container-image-kolla-ansible/commit/6123c7039383dd8a0bcafae993b0d991d2dfc9cb |
| 2023-12-05 |                                                                                |                                                                                                        |
|            | Use a default quotaclass if none is set (#151)                                 | https://github.com/osism/openstack-project-manager/commit/6ebb7da27e77c296f9558ceea4bd973613bac1db     |
|            | Fix logging (#152)                                                             | https://github.com/osism/openstack-project-manager/commit/b3df08be18885460ffa24205b05b62cdd9dc3600     |
|            | Handle default quota class on okeanos projects (#153)                          | https://github.com/osism/openstack-project-manager/commit/e6a8ad838b7502e1ebfd9e42b2714d45e51874aa     |
|            | Assign admin user on already created projects (#154)                           | https://github.com/osism/openstack-project-manager/commit/d1a519136d0fe9e5a9dbe99dc45d10bb4a653c96     |
|            | Improve okeanos quota class (#155)                                             | https://github.com/osism/openstack-project-manager/commit/ecca703732891ee04d08a787530b79d90405f78c     |
|            | Add volume types to quota classes (#156)                                       | https://github.com/osism/openstack-project-manager/commit/b974ee12136a899ba4cf5a48080abc7012e31393     |
|            | configuration-guide: add ceph lvm devices (#213)                               | https://github.com/osism/osism.github.io/commit/bcc57704884bddf2057738d513c575dc8394481e               |
|            | Add some more sections to the ceph configuration guide (#214)                  | https://github.com/osism/osism.github.io/commit/3dbfe6b80dafdbe4ec24ea7e5f3fa8c17ca32552               |
|            | Move parts of ceph ops into the ceph config guide (#216)                       | https://github.com/osism/osism.github.io/commit/f14a61c206e312256672504ee6c209f7ad91ee24               |
|            | Remove ireallymeanit prompt from configure-lvm-volumes play (#339)             | https://github.com/osism/ansible-playbooks/commit/6fca72b111eadf3c0a4e8ce19ad6fde4f7e12283             |
|            | In configure-lvm-volumes always output the generated config (#340)             | https://github.com/osism/ansible-playbooks/commit/71a7ea04d7979d8563459cbf77677ad8d54c40dd             |
|            | Improve create-lvm-devices play (#341)                                         | https://github.com/osism/ansible-playbooks/commit/f2b90189df5ba6659ee8515a168a513c1773b217             |
|            | List missing ceph plays (#466)                                                 | https://github.com/osism/container-image-osism-ansible/commit/200865ea52e107525b14d70a244d499b334741a4 |
| 2023-12-06 |                                                                                |                                                                                                        |
|            | Add public network to quota classes (#157)                                     | https://github.com/osism/openstack-project-manager/commit/a234d2ec40ffee716f842f342947826e0a27c5ec     |
|            | openstack: boot the test instance from a volume (#209)                         | https://github.com/osism/cloud-in-a-box/commit/94cdceb8f0f65e48208bc58f31df8c6929297ce4                |
| 2023-12-07 |                                                                                |                                                                                                        |
|            | Add more storage on the okeanos class (#158)                                   | https://github.com/osism/openstack-project-manager/commit/adc432990fae217893988898024ad49f566e1302     |
|            | Only assign member & load-balancer_member as default roles (#159)              | https://github.com/osism/openstack-project-manager/commit/6052573fe259146bffaccc1a80738494bdaee996     |
|            | Cache roles (#160)                                                             | https://github.com/osism/openstack-project-manager/commit/236a21a378291fa121459fc4a1068f7553d44943     |
|            | Cache admin domain (#161)                                                      | https://github.com/osism/openstack-project-manager/commit/bfdd2c354e181706f35beb5c915c98819c856a31     |
|            | Cache admin users (#162)                                                       | https://github.com/osism/openstack-project-manager/commit/4cba8d40e54386770037e05f9de924935be548c3     |
|            | cloud-in-a-box: 2nd NIC without IP configuration (#219)                        | https://github.com/osism/osism.github.io/commit/150c3c8117d752dd241fcd6e7774b09ca1184b48               |
|            | openstack: add customization of the service configurations (#220)              | https://github.com/osism/osism.github.io/commit/c763d2b330b32c7784d7bd3d9c070e9e1eac79a4               |
|            | Explicitly wait for the manager service (#1887)                                | https://github.com/osism/testbed/commit/de3256595eb122e12340171491f70bc1d876c189                       |
|            | Wait for the pull of all images (#1888)                                        | https://github.com/osism/testbed/commit/264aa8ffcaab744c86953406f71087c27f629bee                       |
|            | Get manager images from osism.harbor.regio.digital (#1889)                     | https://github.com/osism/testbed/commit/1fbe01a8c3896ca1f139b4f8ebc5dc5910c54382                       |
|            | manager: ensure that all containers are up (#1234)                             | https://github.com/osism/ansible-collection-services/commit/810677e08dc768330f84d4e6eb66a41587802cfd   |
|            | manager: ensure that all containers are up (pt. 2) (#1235)                     | https://github.com/osism/ansible-collection-services/commit/c5e585b57140e8f16026c7c22859d87b76b19dca   |
|            | manager: wait for manager service to start (#1236)                             | https://github.com/osism/ansible-collection-services/commit/97eba56d61a21d46b53efcf8053f2fb4e913082c   |
|            | manager: after forced break ensure that all containers are up (#1237)          | https://github.com/osism/ansible-collection-services/commit/1108db5413a030dba2e7d2f4645cb8dedb35f3ed   |
| 2023-12-08 |                                                                                |                                                                                                        |
|            | Add a link to all available OpenStack components (#222)                        | https://github.com/osism/osism.github.io/commit/346911c31175ebd1d424fad69d28fe0a18f4c069               |
|            | ceph: set auth allow insecure global id reclaim = false (#1891)                | https://github.com/osism/testbed/commit/c6e84db66c7cdab2a2dc6d25eefdbd8f39755825                       |
|            | Use the HWE kernel on all nodes (#1892)                                        | https://github.com/osism/testbed/commit/fd736ed3a7e3a6ec8d47b4508622f2f60b05c706                       |
|            | List missing openstack plays (#467)                                            | https://github.com/osism/container-image-osism-ansible/commit/544612b455161a2e3441e58535b7393c3abd31ce |
| 2023-12-09 |                                                                                |                                                                                                        |
| 2023-12-10 |                                                                                |                                                                                                        |
| 2023-12-11 |                                                                                |                                                                                                        |
|            | resource-manager: add sample outputs (#224)                                    | https://github.com/osism/osism.github.io/commit/13ea9864040bc70900a1cabc10b2662968eb38ff               |
|            | Install huey (#729)                                                            | https://github.com/osism/python-osism/commit/16d9381bbd66ec4d34c9ae1fe0f693c510f15501                  |
|            | mirror: connect with S3 API first & improve logging (#706)                     | https://github.com/osism/openstack-image-manager/commit/a522726aaa4d961fd6ea454f565c421542447651       |
| 2023-12-12 |                                                                                |                                                                                                        |
| 2023-12-13 |                                                                                |                                                                                                        |
|            | ops/openstack: add host aggregates playbook (#225)                             | https://github.com/osism/osism.github.io/commit/48ec6b3e9f137ab6ed451991ffd8b2c24146d96c               |
|            | Use info block in image manager section (#226)                                 | https://github.com/osism/osism.github.io/commit/b30a667d6ade6aa4f00443ff3c0d191c24d27334               |
|            | Add new compute node (#227)                                                    | https://github.com/osism/osism.github.io/commit/e3d98973a9b6d46638852b367ea45d599ca24a26               |
|            | Add IPv6 fabric underlay node configuration                                    | https://github.com/osism/osism.github.io/commit/9f8d1c1e73f77f99e5135023a4e9582020312dda               |
|            | Describe how to enable & check nested virtualisation (#229)                    | https://github.com/osism/osism.github.io/commit/120847c29881dd19d626be8282742951315ad164               |
|            | Use y/Y (#230)                                                                 | https://github.com/osism/osism.github.io/commit/07ca889c2293d418a12bac1fcb7872983fb942f8               |
|            | Add netdata & frr on new nodes (#231)                                          | https://github.com/osism/osism.github.io/commit/0f92ce1ee8d8d997bd77fed1c408089af9011a63               |
|            | Add sample custom play (#232)                                                  | https://github.com/osism/osism.github.io/commit/2db166ecb6ede955f7b037315af92f247aa866d2               |
|            | Use docusaurus 3.0.1 (#233)                                                    | https://github.com/osism/osism.github.io/commit/abd66b00d1fe8f08f950c3b8a78e6c0983b74f1d               |
|            | Add containers running on a compute node (#234)                                | https://github.com/osism/osism.github.io/commit/e50ec93fe53ba8a0dba803ea502da47ee7d7c6c4               |
|            | Fix syntax (#235)                                                              | https://github.com/osism/osism.github.io/commit/f7e8bdffed2e1d8406babed66cddce1703d1c04e               |
| 2023-12-14 |                                                                                |                                                                                                        |
|            | Add nova ops section (#236)                                                    | https://github.com/osism/osism.github.io/commit/1b654a6dbc564805ffc61dced95736f0b5507413               |
|            | Log when an image is not deleted because current count < last (#708)           | https://github.com/osism/openstack-image-manager/commit/1fc6468f235b7bf3fd8fa3921781b8fe79c2ee60       |
| 2023-12-15 |                                                                                |                                                                                                        |
|            | Use testbed-node-0 (#237)                                                      | https://github.com/osism/osism.github.io/commit/6eacad92302b023096317b391faaf96c558a9029               |
| 2023-12-16 |                                                                                |                                                                                                        |
| 2023-12-17 |                                                                                |                                                                                                        |
| 2023-12-18 |                                                                                |                                                                                                        |
|            | Pin openstack images (#238)                                                    | https://github.com/osism/osism.github.io/commit/c85d07352e8b1a6ddd55705b13d5ff50da3e0b90               |
|            | Reserve compute node resources (#239)                                          | https://github.com/osism/osism.github.io/commit/bcb8a070fa900997b65b0bd24365a366bf0d4f54               |
|            | Add "OSISM Identity & Access Management" (#240)                                | https://github.com/osism/osism.github.io/commit/5bf616b1f39f894b60b2e9811cd6edb4f1dd8f41               |
|            | Improve home page (#241)                                                       | https://github.com/osism/osism.github.io/commit/05829c73f4f55a8da7c8716c331f2b7b41a65872               |
|            | Add link to SCS project (#242)                                                 | https://github.com/osism/osism.github.io/commit/1af0ece7626a532c76b19ee3664caa29cb932939               |
|            | Change logo (#243)                                                             | https://github.com/osism/osism.github.io/commit/9da8c1a3a4b17e2bc236de6029abf4070bc54197               |
|            | Add link to REGIO (#244)                                                       | https://github.com/osism/osism.github.io/commit/0cde824e842410b02d3e7075b17bcdf31c9a56e8               |
|            | Remove duplicate title from the home page (#245)                               | https://github.com/osism/osism.github.io/commit/533df9b52c198a3bb3bea707fa6e6c9df89300e4               |
|            | Update colors (#247)                                                           | https://github.com/osism/osism.github.io/commit/a01b200c3c5ff9c27ffa3405fa89b6acb1db8e5b               |
|            | Add imprint (#248)                                                             | https://github.com/osism/osism.github.io/commit/7fe98293ac466f541b66d86258330fa98c9dd70a               |
|            | Add local ssd on nova compute nodes (#249)                                     | https://github.com/osism/osism.github.io/commit/bb64e36ab111829918ebb176bacb827fe7df5045               |
|            | Add netdata to the home page (#250)                                            | https://github.com/osism/osism.github.io/commit/ab64a23525bcbf6a3f1ead10efb1070c00569fd1               |
|            | Add privacy page (#251)                                                        | https://github.com/osism/osism.github.io/commit/3bd1c9c9d1aaa0d9e5a2733bfa055c937bbdc918               |
|            | Add 1.29 image (#213)                                                          | https://github.com/osism/k8s-capi-images/commit/315d259113f2a4b5eacbfe52e65e4d2a89db8d62               |
|            | README: remove "Images provided by Vexxhost" (#214)                            | https://github.com/osism/k8s-capi-images/commit/e3f6b1090b8732f67cadb7b8197013edc0256680               |
|            | Add cirros 0.6.2 image (#710)                                                  | https://github.com/osism/openstack-image-manager/commit/e57862a1b61d74ea25aa7833fe157037981383e2       |
|            | Ensure that images are hidden (#711)                                           | https://github.com/osism/openstack-image-manager/commit/5556e43e73e21881ead0d025d874abd5c21636e6       |
|            | Add kubernetes cap 1.29.0 image (#712)                                         | https://github.com/osism/openstack-image-manager/commit/fa95b7fb4b6406ffc0513ce6f04a6309e0ac82bc       |
|            | Add gardenlinux 1312.1 (#707)                                                  | https://github.com/osism/openstack-image-manager/commit/161d7243cb871d8a6b9137faa9450a3da6d5107c       |
|            | Fix gardenlinux 1312.1 URL (#713)                                              | https://github.com/osism/openstack-image-manager/commit/123e91ac9a0887fb3636370a065bfa4a02356deb       |
| 2023-12-19 |                                                                                |                                                                                                        |
|            | Move imprint -> legals (#252)                                                  | https://github.com/osism/osism.github.io/commit/f29ef0a4ed6e54accac90b9e974a72a9079805a7               |
|            | Fix github urls (#253)                                                         | https://github.com/osism/osism.github.io/commit/f930d1736c8b3b95761d643a982e132a20695ece               |
|            | Add zuul ci link (#254)                                                        | https://github.com/osism/osism.github.io/commit/89cf0a553efa43ae5e73cbecf8693e86f11268fe               |
|            | Use docusaurus-search-local plugin (#255)                                      | https://github.com/osism/osism.github.io/commit/e7e7024d099c97a620df810b3e84de89c9dc23c0               |
|            | Fix yarn.lock after e7e7024d099c97a620df810b3e84de89c9dc23c0 (#256)            | https://github.com/osism/osism.github.io/commit/f91fd86386faac9b9cc599bb38acb7f6b8a13e23               |
|            | Add ceph dashboard (#257)                                                      | https://github.com/osism/osism.github.io/commit/50555feb00f56fcf6c9a992a96d7d5479e4c33ac               |
|            | Improve flavor-manager docs (#258)                                             | https://github.com/osism/osism.github.io/commit/7c56488bf8ecfc9580f1ed850fa132166689806e               |
|            | Run infrastructure deployments in foreground (#1901)                           | https://github.com/osism/testbed/commit/a5e84eb38b311ab79c9063f65bbf5717567c6d02                       |
|            | Run all upgrades in foreground (#1902)                                         | https://github.com/osism/testbed/commit/78803817e2075dd200a02be759d3ea44024dc237                       |
|            | manager: allow arguments in the osism update scripts (#1242)                   | https://github.com/osism/ansible-collection-services/commit/d16419f2b05299f1677b1f67dd848da7b93e4068   |
|            | Add talos linux 1.6.0 (#715)                                                   | https://github.com/osism/openstack-image-manager/commit/0c4b8b7d7a9dcad1f3d668d91636a787bd4a3004       |
|            | Add flatcar 3602.2.3 (#716)                                                    | https://github.com/osism/openstack-image-manager/commit/1a5947bdacfe64b1c2a04405406ff14cbca3806d       |
|            | zuul: add mirror-images job (#717)                                             | https://github.com/osism/openstack-image-manager/commit/0caa0c9e6ce5e1ab3c61219e8cb3094482976bf9       |
|            | zuul: add pre-mirror-images play (#718)                                        | https://github.com/osism/openstack-image-manager/commit/64524f731059b4c9b911776bf178e6a20002598c       |
|            | zuul: use cirros image for integration test (#719)                             | https://github.com/osism/openstack-image-manager/commit/25b55e07eebc1e7f39705a8663bd9abe399b48b9       |
|            | zuul: update minio access & secret keys (#720)                                 | https://github.com/osism/openstack-image-manager/commit/420a4e6b64e8584f0fef7982706c67d4534ba621       |
|            | zuul: rename jobs to avoid overlapping names (#722)                            | https://github.com/osism/openstack-image-manager/commit/f4764e556cd6c84205df256332abfcdc547ffcb7       |
|            | zuul: add python-black job (#723)                                              | https://github.com/osism/openstack-image-manager/commit/57270867ddb8a62e63b5046e501ab5de9a2a3c7a       |
|            | Remove unused container image (#724)                                           | https://github.com/osism/openstack-image-manager/commit/07db0203f03b6b958830284475c85d65200e2d95       |
|            | Add spdx license header (#87)                                                  | https://github.com/osism/openstack-flavor-manager/commit/893d237d0bc610b079e6ff446b6a1cb6c0579a0d      |
|            | Add scs:cpu-type (#89)                                                         | https://github.com/osism/openstack-flavor-manager/commit/d8b19e2b1608008200ce5e19ca0b46434ed5343b      |
|            | Add local storage flavors & extra spec (#90)                                   | https://github.com/osism/openstack-flavor-manager/commit/97e7eb863f9380d50a353884675b02d881c2f412      |
|            | Add hw_rng:allowed extra spec (#91)                                            | https://github.com/osism/openstack-flavor-manager/commit/716dfc1175b1e8441f32bdb5fc7fc0a96308b70f      |
|            | Support local_storage extra spec (#92)                                         | https://github.com/osism/openstack-flavor-manager/commit/dc73761ff19b363f53015222e258186af2378114      |
|            | Extra specs has to be a string or an integer (#94)                             | https://github.com/osism/openstack-flavor-manager/commit/d0b98d5fd9cc98cd402f8a94c400d681445d49b8      |
|            | Add scs:disk0-type (#95)                                                       | https://github.com/osism/openstack-flavor-manager/commit/ecc4082aebe3d615ebb95563f0f60452072e6212      |
|            | Update extra specs on existing flavors (#93)                                   | https://github.com/osism/openstack-flavor-manager/commit/159588d8b2dae62f4ec474a9fb1371419ffb66a6      |
| 2023-12-20 |                                                                                |                                                                                                        |
|            | Add sample flavor (#259)                                                       | https://github.com/osism/osism.github.io/commit/06cf2ff7589e87be0265e8294ca575552635d237               |
|            | Prepare use cases (#260)                                                       | https://github.com/osism/osism.github.io/commit/ce2f6fc96e78d9875cd94830193686374975dca9               |
|            | Assign a floating ip address to the test instance (#210)                       | https://github.com/osism/cloud-in-a-box/commit/5fea2953c39e7df8934ab64bf2ba0c12e9c9aa36                |
|            | Add documentation badge (#68)                                                  | https://github.com/osism/openstack-resource-manager/commit/1b5f4175079cb5d0a457e2d4d59af4acd8208545    |
|            | Remove systohc parameter (#1904)                                               | https://github.com/osism/testbed/commit/563cb96686b8d4eec05b34af0c3fc4b9c7db3488                       |
|            | Wait for pull of images (#1905)                                                | https://github.com/osism/testbed/commit/18e1fb66a38f6d6e68c9d59c90e5994caa0c2a00                       |
|            | Assign a floating ip address to the test instance (#1906)                      | https://github.com/osism/testbed/commit/f42a54a2cd2dd0b17e78ede8ebf096af1180e691                       |
|            | Fix debug output (#1907)                                                       | https://github.com/osism/testbed/commit/433349e1c263660909f46cc05988d0dc69ecc419                       |
|            | Remove local_storage extra spec (#96)                                          | https://github.com/osism/openstack-flavor-manager/commit/767683a58d414088e5b9f751d1dae02006c3ccbf      |
| 2023-12-21 |                                                                                |                                                                                                        |
|            | Add SCS use cases (#261)                                                       | https://github.com/osism/osism.github.io/commit/302920da6a581ae54080ed76fbc1ce8898fee7c3               |
|            | Add SEEBURGER DevCloud (#262)                                                  | https://github.com/osism/osism.github.io/commit/cda6a98e7ea31c3302e694261a61e01cfb057213               |
|            | Remove a compute service (#263)                                                | https://github.com/osism/osism.github.io/commit/9853fc511ca01aa216aaf3e85ff770e31b97da05               |
|            | Reboot a compute node (#264)                                                   | https://github.com/osism/osism.github.io/commit/b05ad89a6e6ed80f32fdbe620ae89ee5ea4cc3be               |
|            | Move compute node removal (#265)                                               | https://github.com/osism/osism.github.io/commit/2b3989d21bb7728fa35ff4d0faf244e0ba933f5f               |
|            | Deploy & bootstrap the ceph dashboard (#266)                                   | https://github.com/osism/osism.github.io/commit/8aa12bf46d3c693de23d94762074ed5b57982cbb               |
|            | Add tagline (#267)                                                             | https://github.com/osism/osism.github.io/commit/d8d0814de23dddffc1b6b3bffa0a63f579737d24               |
|            | Improve tagline (#268)                                                         | https://github.com/osism/osism.github.io/commit/5d9fcb43eea5fe6fdfe087cb96e907558bf855a4               |
|            | Replace lorem ipsum with some short texts (#269)                               | https://github.com/osism/osism.github.io/commit/f5d9830a2cae50017b0c4e2589cd6c47767cf1d5               |
|            | Re-add the sidebars.js file (#270)                                             | https://github.com/osism/osism.github.io/commit/7aa6b15c03ba7c72e8ae831b1c3ca9ab54550c78               |
|            | In the CI use the OSISM CI image (#1736)                                       | https://github.com/osism/testbed/commit/54e248652ecca27d8e7607b4560a7554d5b6e404                       |
|            | zuul: update secrets (#26)                                                     | https://github.com/osism/ci-image/commit/c65f39371c68748c62971a3917bde1c7884ba250                      |
|            | Use docker version 24.0.7 (#27)                                                | https://github.com/osism/ci-image/commit/9933c18c9497db98421043e60626adbe70f3125c                      |
|            | Install HWE kernel & remove snapd (#28)                                        | https://github.com/osism/ci-image/commit/f4e2c603c6204b5ef2e373e48388cf4bcb41e10c                      |
|            | zuul: add irrelevant files (#29)                                               | https://github.com/osism/ci-image/commit/020cd7f9222246fc1fb673be84f50efc55e64331                      |
|            | kolla: add om_enable_rabbitmq_quorum_queues (#151)                             | https://github.com/osism/defaults/commit/6a1c713c8e1beaa5ad89ceecb7c2605880281cb9                      |
|            | Add IS_ZUUL variable (#16)                                                     | https://github.com/osism/terraform-base/commit/78d3152fc7406a0209d83ccf9dc9ff9035aefbc0                |
|            | cirrus: update secrets (#216)                                                  | https://github.com/osism/k8s-capi-images/commit/441d721f78f653d36dab87fd17cfeded5af94c5e               |
|            | Cleanup .gitignore file (#725)                                                 | https://github.com/osism/openstack-image-manager/commit/129ac4e426b9b67600543b3370a3a8de6a264781       |
|            | Remove old gardenlinux images (#721)                                           | https://github.com/osism/openstack-image-manager/commit/78cccf348c1909cd6e07d7990273ba53a21ca93d       |
|            | Add OSISM CI image (#726)                                                      | https://github.com/osism/openstack-image-manager/commit/7a513d8d1f0887bb44c4e6bc734350ddf8deb32d       |
| 2023-12-22 |                                                                                |                                                                                                        |
|            | zuul: overall improvements (#1911)                                             | https://github.com/osism/testbed/commit/2fc95e81d89d0704048166f7f5306e307b608087                       |
|            | manager: set ara_server_mariadb_volume_type = tmpfs (#1914)                    | https://github.com/osism/testbed/commit/706b32e6b6c4f46249dcc324a0023af352aaf87d                       |
|            | Make sure that rngd is available on the manager from the start (#1915)         | https://github.com/osism/testbed/commit/65add81968b2c0e8745794c2bd2955cdc4abe3b0                       |
|            | infrastructure: set netbox_postgres_volume_type = tmpfs (#1916)                | https://github.com/osism/testbed/commit/eae6953e7fb466b38182384cb742cc3aa103e46c                       |
|            | Always deploy monitoring services (#17)                                        | https://github.com/osism/terraform-base/commit/c2ec76494e845c01c26c4bedc866235f30b2567d                |
|            | manager: add ara_server_mariadb_volume_type parameter (#1244)                  | https://github.com/osism/ansible-collection-services/commit/2f9a09c624216459ad1431a0f37f4aeeec0ec8b3   |
|            | netbox: add netbox_postgres_volume_type parameter (#1245)                      | https://github.com/osism/ansible-collection-services/commit/9fd88f8c0de92e336b1ecf372e1bc6952eafcbed   |
| 2023-12-23 |                                                                                |                                                                                                        |
|            | Update default flavor & image (#52)                                            | https://github.com/osism/openstack-simple-stress/commit/eaa9867c6a3aa40504ef04918c22ac13bcf3e72d       |
|            | Improve log format (#53)                                                       | https://github.com/osism/openstack-simple-stress/commit/6f52fd5477ef74e5b9a2e5d4a0829bde19de9b99       |
|            | Use SCS-1V-1-10 as default flavor (#54)                                        | https://github.com/osism/openstack-simple-stress/commit/53b2cb80aa991d7a0fd357e6ccc19a03c9d77f33       |
| 2023-12-24 |                                                                                |                                                                                                        |
|            | Improve title & subtitle (#271)                                                | https://github.com/osism/osism.github.io/commit/e677f497d4ee692e9570d0431433587246a0a33f               |
|            | Add cinder scripts from sapcc/openstack-nannies (#69)                          | https://github.com/osism/openstack-resource-manager/commit/784573679f58d1e6570ca1e487af8214b5687847    |
|            | Only change the registry when running in the CI (#1917)                        | https://github.com/osism/testbed/commit/ee3308d621031d8056f4a990e16a036265ab9ca2                       |
|            | Deployment of squid is part of the manager service only (#1918)                | https://github.com/osism/testbed/commit/b265e9c623f333bd3749002ab1375fe65e684e7e                       |
| 2023-12-25 |                                                                                |                                                                                                        |
| 2023-12-26 |                                                                                |                                                                                                        |
| 2023-12-27 |                                                                                |                                                                                                        |
| 2023-12-28 |                                                                                |                                                                                                        |
|            | Remove glance parameters because of OSSN-0090 (#1920)                          | https://github.com/osism/testbed/commit/d27abf43e4847f4c546f49e2378ccfc5c50e5832                       |
|            | Cleanup packages on the manager (#1919)                                        | https://github.com/osism/testbed/commit/c1fd4953deebc3f2de2576239dd1f7d6976ccfdb                       |
|            | Try to import images from the image cache (#1921)                              | https://github.com/osism/testbed/commit/c4621952bf9e410677eeb54c654920865d653ae9                       |
|            | Wait for custom import-images play (#1922)                                     | https://github.com/osism/testbed/commit/bd4ddeac6a44a2b90f65cbc91d0c1b2e31ab43b0                       |
|            | Sync ceph dashboards with upstream (#36)                                       | https://github.com/osism/kolla-operations/commit/02c267c70d1b564cfa2b76bb8fdf6956d0da8f60              |
|            | Sync openstack dashboard with upstream (#37)                                   | https://github.com/osism/kolla-operations/commit/7a4c8a31362997524b5c73dc16254c06cf5dfdaa              |
|            | Remove old files & cleanup README (#38)                                        | https://github.com/osism/kolla-operations/commit/3265f1afe471d4f263e781caddcb180b7d9e6b5c              |
|            | Install ansible-core instead of ansible (#30)                                  | https://github.com/osism/ci-image/commit/932c47ddbc674f7e0f65a9976d4c455e4260b9ab                      |
|            | Add .images.yml (#31)                                                          | https://github.com/osism/ci-image/commit/6cc96f4ec0d3a7292e25d23075eb139f4f2847e8                      |
|            | Preload stable container images (#32)                                          | https://github.com/osism/ci-image/commit/9e07621ddc5d725d1e1c72ab8a3022967db74eec                      |
|            | Import inventory-reconciler image (#33)                                        | https://github.com/osism/ci-image/commit/ddc08ea680b51e53c527c04114aebd109263387f                      |
|            | Import netbox image (#34)                                                      | https://github.com/osism/ci-image/commit/4711ca93d6b611cfcb12c72afbe061e1be5dd553                      |
| 2023-12-29 |                                                                                |                                                                                                        |
|            | Add project logos (#272)                                                       | https://github.com/osism/osism.github.io/commit/ddb612902ad8708d70a56a0212ba3fd021554578               |
|            | Fix ansible-lint issues (#1924)                                                | https://github.com/osism/testbed/commit/e81e7bea73fbdbb60054f96883ad9b573ddc2fcc                       |
|            | Do not pull images with docker-compose service (#1923)                         | https://github.com/osism/testbed/commit/468133c87c553904ac2b4fb4d4b54c58b10c858b                       |
| 2023-12-30 |                                                                                |                                                                                                        |
|            | Import images via cloud-init (#1926)                                           | https://github.com/osism/testbed/commit/1144aac9eecba0ae174b6119b67334d5f8c02f95                       |
|            | Ensure that the squid service is up and running (#1927)                        | https://github.com/osism/testbed/commit/3fc9efdbac4718d09508df86c890b26735d78c5f                       |
|            | Wait up to 10 minutes until boot of manager finished (#1928)                   | https://github.com/osism/testbed/commit/ed6b8490c6d54ca7d7cb409014659efba6e1364b                       |
|            | Revert "Do not pull images with docker-compose service (#1923)" (#1929)        | https://github.com/osism/testbed/commit/e6457e7cc6395dccf86a39d66a0045f677d69a6a                       |
|            | Add /etc/osism-ci-image file (#35)                                             | https://github.com/osism/ci-image/commit/7a65d745fdaa3cca435c268b52eb50653c37a930                      |
|            | Move images to /opt/images (#36)                                               | https://github.com/osism/ci-image/commit/75d0c077f1c323a7f059ec0bac4972d5e4c10c44                      |
|            | Use debian bookworm as base image (#470)                                       | https://github.com/osism/container-image-osism-ansible/commit/3307602d2b3fcc613cbb559b24b8ae5eef4e86ed |
|            | testbed-default: use osism-testbed.sh script for all first boot commands (#18) | https://github.com/osism/terraform-base/commit/f940ebadc1d9fd7fbcc3f2ee25e7914f181b5546                |
|            | testbed-default: import stable images when using the OSISM CI image (#19)      | https://github.com/osism/terraform-base/commit/b36b37a736a101f0de667cb83a510410d37d3fdb                |
|            | Fix "Invalid cloud-config schema: user-data" (#20)                             | https://github.com/osism/terraform-base/commit/6366405feff2d1c2eebb55d9912005e6e5a8c878                |
|            | Only import stable manager images when deploying a stable manager (#21)        | https://github.com/osism/terraform-base/commit/4ea0ccd58dc39c989ff4352fb7b920a07fa0c63e                |
|            | Revert "Fix "Invalid cloud-config schema: user-data" (#20)" (#22)              | https://github.com/osism/terraform-base/commit/f588f5756beeccd84caaaa8fe1b21a40d0fd9615                |
|            | openstackclient: improve service start (#1246)                                 | https://github.com/osism/ansible-collection-services/commit/4607a0dc3a2f997305e4de2c0be0d20b251eed72   |
| 2023-12-31 |                                                                                |                                                                                                        |
