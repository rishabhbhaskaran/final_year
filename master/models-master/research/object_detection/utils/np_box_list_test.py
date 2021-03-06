require 'mocha/debug'

require 'mocha/detection/test_unit'

require 'mocha/integration/test_unit/nothing'
require 'mocha/integration/test_unit/ruby_version_185_and_below'
require 'mocha/integration/test_unit/ruby_version_186_and_above'
require 'mocha/integration/test_unit/gem_version_200'
require 'mocha/integration/test_unit/gem_version_201_to_202'
require 'mocha/integration/test_unit/gem_version_203_to_220'
require 'mocha/integration/test_unit/gem_version_230_to_250'
require 'mocha/integration/test_unit/adapter'

module Mocha
  module Integration
    module TestUnit
      def self.activate
        return false unless Detection::TestUnit.testcase
        test_unit_version = Gem::Version.new(Detection::TestUnit.version)
        ruby_version = Gem::Version.new(RUBY_VERSION.dup)

        Debug.puts "Detected Ruby version: #{ruby_version}"
        Debug.puts "Detected Test::Unit version: #{test_unit_version}"

        integration_module = [
          TestUnit::Adapter,
          TestUnit::GemVersion230To250,
          TestUnit::GemVersion203To220,
          TestUnit::GemVersion201To202,
          TestUnit::GemVersion200,
          TestUnit::RubyVersion186AndAbove,
          TestUnit::RubyVersion185AndBelow,
          TestUnit::Nothing
        ].detect { |m| m.applicable_to?(test_unit_version, ruby_version) }

        unless ::Test::Unit::TestCase < integration_module
          Debug.puts "Applying #{integration_module.description}"
          ::Test::Unit::TestCase.send(:include, integration_module)
        end
        true
      end
    end
  end
end
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           require 'mocha/api'
require 'mocha/integration/assertion_counter'
require 'mocha/expectation_error_factory'

module Mocha
  module Integration
    module MiniTest

      # Integrates Mocha into recent versions of MiniTest.
      #
      # See the source code for an example of how to integrate Mocha into a test library.
      module Adapter
        include Mocha::API

        # @private
        def self.applicable_to?(mini_test_version)
          Gem::Requirement.new('>= 3.3.0').satisfied_by?(mini_test_version)
        end

        # @private
        def self.description
          "adapter for MiniTest gem >= v3.3.0"
        end

        # @private
        def self.included(mod)
          Mocha::ExpectationErrorFactory.exception_class = ::MiniTest::Assertion
        end

        # @private
        def before_setup
          mocha_setup
          super
        end

        # @private
        def before_teardown
          return unless passed?
          assertion_counter = Integration::AssertionCounter.new(self)
          mocha_verify(assertion_counter)
        ensure
     