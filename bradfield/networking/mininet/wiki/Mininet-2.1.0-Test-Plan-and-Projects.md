Currently we don't have a large set of tests or a procedure for running them. We would like to create an expanded set of tests to ensure the reliability, functionality, and performance of the Mininet system (and to avoid bug regressions.) Additionally, we should describe procedures for running these tests, both in development and for release testing.

### Mininet 2.1.0 Test Plan

#### Automated tests

We now have an automated VM build and test script for Mininet, `build.py`.

- `build.py` should succeed for {precise,raring,saucy}{32,64}server
-  additionally, launchpad auto-build should succeed

#### Other tests

- All examples in `examples/` should run correctly.
  - We are working on automating this testing
- VM images should download and boot from our VM repository
- Walkthrough should work

### Recommended post-2.1 Test Enhancements

There are several obvious ways that we would like to enhance Mininet's testing, including improving the infrastructure, developing additional tests and test cases, and integrating what we already have.

#### Full build/test/release automation

- Build/test system should upload results to S3
- Build/test should run automatically/nightly on stable infrastructure (not yet available)

#### Enhance unit tests

- All API calls should be tested if possible.
- We should add more tests to the (currently minimal) test suite.
- Additionally, it would be nice to have some notion of code coverage.

#### Automated examples/ tests and system-level tests

We want to have a means of ensuring that the examples don’t break! probably each of the examples should be runnable in “test” mode!!

Ideally many examples can serve as instructive and realistic demonstrations of what Mininet can do, as starter code to build upon, and as system-level tests.

#### Scalability and performance tests!!

A goal of Mininet was "1000 nodes in a laptop" - we really need to identify the true capabilities and scalability of Mininet; I think we should have some tests which you can run to determine the largest network that you can simulate in various modes on Mininet. Ultimately scalability and performance tests should be part of a feedback loop to improve Mininet's performance and to enable scale-up and scale-out (e.g. to the original goal of simulating all of Stanford on a cluster.)

#### General automated builds and testing

We should have an automated system for regularly grabbing current branches of Mininet and making sure that they can be built and run; additionally, we should make it possible to create (and test) VM images easily and in an automated fashion.
