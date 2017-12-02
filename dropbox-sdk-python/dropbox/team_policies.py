# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# @generated
# flake8: noqa
# pylint: skip-file
try:
    from . import stone_validators as bv
    from . import stone_base as bb
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import stone_validators as bv
    import stone_base as bb

class EmmState(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar disabled: Emm token is disabled.
    :ivar optional: Emm token is optional.
    :ivar required: Emm token is required.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    disabled = None
    # Attribute is overwritten below the class definition
    optional = None
    # Attribute is overwritten below the class definition
    required = None
    # Attribute is overwritten below the class definition
    other = None

    def is_disabled(self):
        """
        Check if the union tag is ``disabled``.

        :rtype: bool
        """
        return self._tag == 'disabled'

    def is_optional(self):
        """
        Check if the union tag is ``optional``.

        :rtype: bool
        """
        return self._tag == 'optional'

    def is_required(self):
        """
        Check if the union tag is ``required``.

        :rtype: bool
        """
        return self._tag == 'required'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'EmmState(%r, %r)' % (self._tag, self._value)

EmmState_validator = bv.Union(EmmState)

class GroupCreation(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar admins_and_members: Team admins and members can create groups.
    :ivar admins_only: Only team admins can create groups.
    """

    _catch_all = None
    # Attribute is overwritten below the class definition
    admins_and_members = None
    # Attribute is overwritten below the class definition
    admins_only = None

    def is_admins_and_members(self):
        """
        Check if the union tag is ``admins_and_members``.

        :rtype: bool
        """
        return self._tag == 'admins_and_members'

    def is_admins_only(self):
        """
        Check if the union tag is ``admins_only``.

        :rtype: bool
        """
        return self._tag == 'admins_only'

    def __repr__(self):
        return 'GroupCreation(%r, %r)' % (self._tag, self._value)

GroupCreation_validator = bv.Union(GroupCreation)

class OfficeAddInPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar disabled: Office Add-In is disabled.
    :ivar enabled: Office Add-In is enabled.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    disabled = None
    # Attribute is overwritten below the class definition
    enabled = None
    # Attribute is overwritten below the class definition
    other = None

    def is_disabled(self):
        """
        Check if the union tag is ``disabled``.

        :rtype: bool
        """
        return self._tag == 'disabled'

    def is_enabled(self):
        """
        Check if the union tag is ``enabled``.

        :rtype: bool
        """
        return self._tag == 'enabled'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'OfficeAddInPolicy(%r, %r)' % (self._tag, self._value)

OfficeAddInPolicy_validator = bv.Union(OfficeAddInPolicy)

class PaperDeploymentPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar full: All team members have access to Paper.
    :ivar partial: Only whitelisted team members can access Paper. To see which
        user is whitelisted, check 'is_paper_whitelisted' on 'account/info'.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    full = None
    # Attribute is overwritten below the class definition
    partial = None
    # Attribute is overwritten below the class definition
    other = None

    def is_full(self):
        """
        Check if the union tag is ``full``.

        :rtype: bool
        """
        return self._tag == 'full'

    def is_partial(self):
        """
        Check if the union tag is ``partial``.

        :rtype: bool
        """
        return self._tag == 'partial'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'PaperDeploymentPolicy(%r, %r)' % (self._tag, self._value)

PaperDeploymentPolicy_validator = bv.Union(PaperDeploymentPolicy)

class PaperEnabledPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar disabled: Paper is disabled.
    :ivar enabled: Paper is enabled.
    :ivar unspecified: Unspecified policy.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    disabled = None
    # Attribute is overwritten below the class definition
    enabled = None
    # Attribute is overwritten below the class definition
    unspecified = None
    # Attribute is overwritten below the class definition
    other = None

    def is_disabled(self):
        """
        Check if the union tag is ``disabled``.

        :rtype: bool
        """
        return self._tag == 'disabled'

    def is_enabled(self):
        """
        Check if the union tag is ``enabled``.

        :rtype: bool
        """
        return self._tag == 'enabled'

    def is_unspecified(self):
        """
        Check if the union tag is ``unspecified``.

        :rtype: bool
        """
        return self._tag == 'unspecified'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'PaperEnabledPolicy(%r, %r)' % (self._tag, self._value)

PaperEnabledPolicy_validator = bv.Union(PaperEnabledPolicy)

class PasswordStrengthPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar minimal_requirements: User passwords will adhere to the minimal
        password strength policy.
    :ivar moderate_password: User passwords will adhere to the moderate password
        strength policy.
    :ivar strong_password: User passwords will adhere to the very strong
        password strength policy.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    minimal_requirements = None
    # Attribute is overwritten below the class definition
    moderate_password = None
    # Attribute is overwritten below the class definition
    strong_password = None
    # Attribute is overwritten below the class definition
    other = None

    def is_minimal_requirements(self):
        """
        Check if the union tag is ``minimal_requirements``.

        :rtype: bool
        """
        return self._tag == 'minimal_requirements'

    def is_moderate_password(self):
        """
        Check if the union tag is ``moderate_password``.

        :rtype: bool
        """
        return self._tag == 'moderate_password'

    def is_strong_password(self):
        """
        Check if the union tag is ``strong_password``.

        :rtype: bool
        """
        return self._tag == 'strong_password'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'PasswordStrengthPolicy(%r, %r)' % (self._tag, self._value)

PasswordStrengthPolicy_validator = bv.Union(PasswordStrengthPolicy)

class RolloutMethod(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar unlink_all: Unlink all.
    :ivar unlink_most_inactive: Unlink devices with the most inactivity.
    :ivar add_member_to_exceptions: Add member to Exceptions.
    """

    _catch_all = None
    # Attribute is overwritten below the class definition
    unlink_all = None
    # Attribute is overwritten below the class definition
    unlink_most_inactive = None
    # Attribute is overwritten below the class definition
    add_member_to_exceptions = None

    def is_unlink_all(self):
        """
        Check if the union tag is ``unlink_all``.

        :rtype: bool
        """
        return self._tag == 'unlink_all'

    def is_unlink_most_inactive(self):
        """
        Check if the union tag is ``unlink_most_inactive``.

        :rtype: bool
        """
        return self._tag == 'unlink_most_inactive'

    def is_add_member_to_exceptions(self):
        """
        Check if the union tag is ``add_member_to_exceptions``.

        :rtype: bool
        """
        return self._tag == 'add_member_to_exceptions'

    def __repr__(self):
        return 'RolloutMethod(%r, %r)' % (self._tag, self._value)

RolloutMethod_validator = bv.Union(RolloutMethod)

class SharedFolderJoinPolicy(bb.Union):
    """
    Policy governing which shared folders a team member can join.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar from_team_only: Team members can only join folders shared by
        teammates.
    :ivar from_anyone: Team members can join any shared folder, including those
        shared by users outside the team.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    from_team_only = None
    # Attribute is overwritten below the class definition
    from_anyone = None
    # Attribute is overwritten below the class definition
    other = None

    def is_from_team_only(self):
        """
        Check if the union tag is ``from_team_only``.

        :rtype: bool
        """
        return self._tag == 'from_team_only'

    def is_from_anyone(self):
        """
        Check if the union tag is ``from_anyone``.

        :rtype: bool
        """
        return self._tag == 'from_anyone'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SharedFolderJoinPolicy(%r, %r)' % (self._tag, self._value)

SharedFolderJoinPolicy_validator = bv.Union(SharedFolderJoinPolicy)

class SharedFolderMemberPolicy(bb.Union):
    """
    Policy governing who can be a member of a folder shared by a team member.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar team: Only a teammate can be a member of a folder shared by a team
        member.
    :ivar anyone: Anyone can be a member of a folder shared by a team member.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    team = None
    # Attribute is overwritten below the class definition
    anyone = None
    # Attribute is overwritten below the class definition
    other = None

    def is_team(self):
        """
        Check if the union tag is ``team``.

        :rtype: bool
        """
        return self._tag == 'team'

    def is_anyone(self):
        """
        Check if the union tag is ``anyone``.

        :rtype: bool
        """
        return self._tag == 'anyone'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SharedFolderMemberPolicy(%r, %r)' % (self._tag, self._value)

SharedFolderMemberPolicy_validator = bv.Union(SharedFolderMemberPolicy)

class SharedLinkCreatePolicy(bb.Union):
    """
    Policy governing the visibility of shared links. This policy can apply to
    newly created shared links, or all shared links.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar default_public: By default, anyone can access newly created shared
        links. No login will be required to access the shared links unless
        overridden.
    :ivar default_team_only: By default, only members of the same team can
        access newly created shared links. Login will be required to access the
        shared links unless overridden.
    :ivar team_only: Only members of the same team can access all shared links.
        Login will be required to access all shared links.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    default_public = None
    # Attribute is overwritten below the class definition
    default_team_only = None
    # Attribute is overwritten below the class definition
    team_only = None
    # Attribute is overwritten below the class definition
    other = None

    def is_default_public(self):
        """
        Check if the union tag is ``default_public``.

        :rtype: bool
        """
        return self._tag == 'default_public'

    def is_default_team_only(self):
        """
        Check if the union tag is ``default_team_only``.

        :rtype: bool
        """
        return self._tag == 'default_team_only'

    def is_team_only(self):
        """
        Check if the union tag is ``team_only``.

        :rtype: bool
        """
        return self._tag == 'team_only'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SharedLinkCreatePolicy(%r, %r)' % (self._tag, self._value)

SharedLinkCreatePolicy_validator = bv.Union(SharedLinkCreatePolicy)

class SmartSyncPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar local: The specified content will be synced as local files by default.
    :ivar on_demand: The specified content will be synced as on-demand files by
        default.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    local = None
    # Attribute is overwritten below the class definition
    on_demand = None
    # Attribute is overwritten below the class definition
    other = None

    def is_local(self):
        """
        Check if the union tag is ``local``.

        :rtype: bool
        """
        return self._tag == 'local'

    def is_on_demand(self):
        """
        Check if the union tag is ``on_demand``.

        :rtype: bool
        """
        return self._tag == 'on_demand'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SmartSyncPolicy(%r, %r)' % (self._tag, self._value)

SmartSyncPolicy_validator = bv.Union(SmartSyncPolicy)

class SsoPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar disabled: Users will be able to sign in with their Dropbox
        credentials.
    :ivar optional: Users will be able to sign in with either their Dropbox or
        single sign-on credentials.
    :ivar required: Users will be required to sign in with their single sign-on
        credentials.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    disabled = None
    # Attribute is overwritten below the class definition
    optional = None
    # Attribute is overwritten below the class definition
    required = None
    # Attribute is overwritten below the class definition
    other = None

    def is_disabled(self):
        """
        Check if the union tag is ``disabled``.

        :rtype: bool
        """
        return self._tag == 'disabled'

    def is_optional(self):
        """
        Check if the union tag is ``optional``.

        :rtype: bool
        """
        return self._tag == 'optional'

    def is_required(self):
        """
        Check if the union tag is ``required``.

        :rtype: bool
        """
        return self._tag == 'required'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SsoPolicy(%r, %r)' % (self._tag, self._value)

SsoPolicy_validator = bv.Union(SsoPolicy)

class TeamMemberPolicies(object):
    """
    Policies governing team members.

    :ivar sharing: Policies governing sharing.
    :ivar emm_state: This describes the Enterprise Mobility Management (EMM)
        state for this team. This information can be used to understand if an
        organization is integrating with a third-party EMM vendor to further
        manage and apply restrictions upon the team's Dropbox usage on mobile
        devices. This is a new feature and in the future we'll be adding more
        new fields and additional documentation.
    :ivar office_addin: The admin policy around the Dropbox Office Add-In for
        this team.
    """

    __slots__ = [
        '_sharing_value',
        '_sharing_present',
        '_emm_state_value',
        '_emm_state_present',
        '_office_addin_value',
        '_office_addin_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 sharing=None,
                 emm_state=None,
                 office_addin=None):
        self._sharing_value = None
        self._sharing_present = False
        self._emm_state_value = None
        self._emm_state_present = False
        self._office_addin_value = None
        self._office_addin_present = False
        if sharing is not None:
            self.sharing = sharing
        if emm_state is not None:
            self.emm_state = emm_state
        if office_addin is not None:
            self.office_addin = office_addin

    @property
    def sharing(self):
        """
        Policies governing sharing.

        :rtype: TeamSharingPolicies
        """
        if self._sharing_present:
            return self._sharing_value
        else:
            raise AttributeError("missing required field 'sharing'")

    @sharing.setter
    def sharing(self, val):
        self._sharing_validator.validate_type_only(val)
        self._sharing_value = val
        self._sharing_present = True

    @sharing.deleter
    def sharing(self):
        self._sharing_value = None
        self._sharing_present = False

    @property
    def emm_state(self):
        """
        This describes the Enterprise Mobility Management (EMM) state for this
        team. This information can be used to understand if an organization is
        integrating with a third-party EMM vendor to further manage and apply
        restrictions upon the team's Dropbox usage on mobile devices. This is a
        new feature and in the future we'll be adding more new fields and
        additional documentation.

        :rtype: EmmState
        """
        if self._emm_state_present:
            return self._emm_state_value
        else:
            raise AttributeError("missing required field 'emm_state'")

    @emm_state.setter
    def emm_state(self, val):
        self._emm_state_validator.validate_type_only(val)
        self._emm_state_value = val
        self._emm_state_present = True

    @emm_state.deleter
    def emm_state(self):
        self._emm_state_value = None
        self._emm_state_present = False

    @property
    def office_addin(self):
        """
        The admin policy around the Dropbox Office Add-In for this team.

        :rtype: OfficeAddInPolicy
        """
        if self._office_addin_present:
            return self._office_addin_value
        else:
            raise AttributeError("missing required field 'office_addin'")

    @office_addin.setter
    def office_addin(self, val):
        self._office_addin_validator.validate_type_only(val)
        self._office_addin_value = val
        self._office_addin_present = True

    @office_addin.deleter
    def office_addin(self):
        self._office_addin_value = None
        self._office_addin_present = False

    def __repr__(self):
        return 'TeamMemberPolicies(sharing={!r}, emm_state={!r}, office_addin={!r})'.format(
            self._sharing_value,
            self._emm_state_value,
            self._office_addin_value,
        )

TeamMemberPolicies_validator = bv.Struct(TeamMemberPolicies)

class TeamSharingPolicies(object):
    """
    Policies governing sharing within and outside of the team.

    :ivar shared_folder_member_policy: Who can join folders shared by team
        members.
    :ivar shared_folder_join_policy: Which shared folders team members can join.
    :ivar shared_link_create_policy: Who can view shared links owned by team
        members.
    """

    __slots__ = [
        '_shared_folder_member_policy_value',
        '_shared_folder_member_policy_present',
        '_shared_folder_join_policy_value',
        '_shared_folder_join_policy_present',
        '_shared_link_create_policy_value',
        '_shared_link_create_policy_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 shared_folder_member_policy=None,
                 shared_folder_join_policy=None,
                 shared_link_create_policy=None):
        self._shared_folder_member_policy_value = None
        self._shared_folder_member_policy_present = False
        self._shared_folder_join_policy_value = None
        self._shared_folder_join_policy_present = False
        self._shared_link_create_policy_value = None
        self._shared_link_create_policy_present = False
        if shared_folder_member_policy is not None:
            self.shared_folder_member_policy = shared_folder_member_policy
        if shared_folder_join_policy is not None:
            self.shared_folder_join_policy = shared_folder_join_policy
        if shared_link_create_policy is not None:
            self.shared_link_create_policy = shared_link_create_policy

    @property
    def shared_folder_member_policy(self):
        """
        Who can join folders shared by team members.

        :rtype: SharedFolderMemberPolicy
        """
        if self._shared_folder_member_policy_present:
            return self._shared_folder_member_policy_value
        else:
            raise AttributeError("missing required field 'shared_folder_member_policy'")

    @shared_folder_member_policy.setter
    def shared_folder_member_policy(self, val):
        self._shared_folder_member_policy_validator.validate_type_only(val)
        self._shared_folder_member_policy_value = val
        self._shared_folder_member_policy_present = True

    @shared_folder_member_policy.deleter
    def shared_folder_member_policy(self):
        self._shared_folder_member_policy_value = None
        self._shared_folder_member_policy_present = False

    @property
    def shared_folder_join_policy(self):
        """
        Which shared folders team members can join.

        :rtype: SharedFolderJoinPolicy
        """
        if self._shared_folder_join_policy_present:
            return self._shared_folder_join_policy_value
        else:
            raise AttributeError("missing required field 'shared_folder_join_policy'")

    @shared_folder_join_policy.setter
    def shared_folder_join_policy(self, val):
        self._shared_folder_join_policy_validator.validate_type_only(val)
        self._shared_folder_join_policy_value = val
        self._shared_folder_join_policy_present = True

    @shared_folder_join_policy.deleter
    def shared_folder_join_policy(self):
        self._shared_folder_join_policy_value = None
        self._shared_folder_join_policy_present = False

    @property
    def shared_link_create_policy(self):
        """
        Who can view shared links owned by team members.

        :rtype: SharedLinkCreatePolicy
        """
        if self._shared_link_create_policy_present:
            return self._shared_link_create_policy_value
        else:
            raise AttributeError("missing required field 'shared_link_create_policy'")

    @shared_link_create_policy.setter
    def shared_link_create_policy(self, val):
        self._shared_link_create_policy_validator.validate_type_only(val)
        self._shared_link_create_policy_value = val
        self._shared_link_create_policy_present = True

    @shared_link_create_policy.deleter
    def shared_link_create_policy(self):
        self._shared_link_create_policy_value = None
        self._shared_link_create_policy_present = False

    def __repr__(self):
        return 'TeamSharingPolicies(shared_folder_member_policy={!r}, shared_folder_join_policy={!r}, shared_link_create_policy={!r})'.format(
            self._shared_folder_member_policy_value,
            self._shared_folder_join_policy_value,
            self._shared_link_create_policy_value,
        )

TeamSharingPolicies_validator = bv.Struct(TeamSharingPolicies)

class TwoStepVerificationPolicy(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar require_tfa_enable: Enabled require two factor authorization.
    :ivar require_tfa_disable: Disabled require two factor authorization.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    require_tfa_enable = None
    # Attribute is overwritten below the class definition
    require_tfa_disable = None
    # Attribute is overwritten below the class definition
    other = None

    def is_require_tfa_enable(self):
        """
        Check if the union tag is ``require_tfa_enable``.

        :rtype: bool
        """
        return self._tag == 'require_tfa_enable'

    def is_require_tfa_disable(self):
        """
        Check if the union tag is ``require_tfa_disable``.

        :rtype: bool
        """
        return self._tag == 'require_tfa_disable'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'TwoStepVerificationPolicy(%r, %r)' % (self._tag, self._value)

TwoStepVerificationPolicy_validator = bv.Union(TwoStepVerificationPolicy)

EmmState._disabled_validator = bv.Void()
EmmState._optional_validator = bv.Void()
EmmState._required_validator = bv.Void()
EmmState._other_validator = bv.Void()
EmmState._tagmap = {
    'disabled': EmmState._disabled_validator,
    'optional': EmmState._optional_validator,
    'required': EmmState._required_validator,
    'other': EmmState._other_validator,
}

EmmState.disabled = EmmState('disabled')
EmmState.optional = EmmState('optional')
EmmState.required = EmmState('required')
EmmState.other = EmmState('other')

GroupCreation._admins_and_members_validator = bv.Void()
GroupCreation._admins_only_validator = bv.Void()
GroupCreation._tagmap = {
    'admins_and_members': GroupCreation._admins_and_members_validator,
    'admins_only': GroupCreation._admins_only_validator,
}

GroupCreation.admins_and_members = GroupCreation('admins_and_members')
GroupCreation.admins_only = GroupCreation('admins_only')

OfficeAddInPolicy._disabled_validator = bv.Void()
OfficeAddInPolicy._enabled_validator = bv.Void()
OfficeAddInPolicy._other_validator = bv.Void()
OfficeAddInPolicy._tagmap = {
    'disabled': OfficeAddInPolicy._disabled_validator,
    'enabled': OfficeAddInPolicy._enabled_validator,
    'other': OfficeAddInPolicy._other_validator,
}

OfficeAddInPolicy.disabled = OfficeAddInPolicy('disabled')
OfficeAddInPolicy.enabled = OfficeAddInPolicy('enabled')
OfficeAddInPolicy.other = OfficeAddInPolicy('other')

PaperDeploymentPolicy._full_validator = bv.Void()
PaperDeploymentPolicy._partial_validator = bv.Void()
PaperDeploymentPolicy._other_validator = bv.Void()
PaperDeploymentPolicy._tagmap = {
    'full': PaperDeploymentPolicy._full_validator,
    'partial': PaperDeploymentPolicy._partial_validator,
    'other': PaperDeploymentPolicy._other_validator,
}

PaperDeploymentPolicy.full = PaperDeploymentPolicy('full')
PaperDeploymentPolicy.partial = PaperDeploymentPolicy('partial')
PaperDeploymentPolicy.other = PaperDeploymentPolicy('other')

PaperEnabledPolicy._disabled_validator = bv.Void()
PaperEnabledPolicy._enabled_validator = bv.Void()
PaperEnabledPolicy._unspecified_validator = bv.Void()
PaperEnabledPolicy._other_validator = bv.Void()
PaperEnabledPolicy._tagmap = {
    'disabled': PaperEnabledPolicy._disabled_validator,
    'enabled': PaperEnabledPolicy._enabled_validator,
    'unspecified': PaperEnabledPolicy._unspecified_validator,
    'other': PaperEnabledPolicy._other_validator,
}

PaperEnabledPolicy.disabled = PaperEnabledPolicy('disabled')
PaperEnabledPolicy.enabled = PaperEnabledPolicy('enabled')
PaperEnabledPolicy.unspecified = PaperEnabledPolicy('unspecified')
PaperEnabledPolicy.other = PaperEnabledPolicy('other')

PasswordStrengthPolicy._minimal_requirements_validator = bv.Void()
PasswordStrengthPolicy._moderate_password_validator = bv.Void()
PasswordStrengthPolicy._strong_password_validator = bv.Void()
PasswordStrengthPolicy._other_validator = bv.Void()
PasswordStrengthPolicy._tagmap = {
    'minimal_requirements': PasswordStrengthPolicy._minimal_requirements_validator,
    'moderate_password': PasswordStrengthPolicy._moderate_password_validator,
    'strong_password': PasswordStrengthPolicy._strong_password_validator,
    'other': PasswordStrengthPolicy._other_validator,
}

PasswordStrengthPolicy.minimal_requirements = PasswordStrengthPolicy('minimal_requirements')
PasswordStrengthPolicy.moderate_password = PasswordStrengthPolicy('moderate_password')
PasswordStrengthPolicy.strong_password = PasswordStrengthPolicy('strong_password')
PasswordStrengthPolicy.other = PasswordStrengthPolicy('other')

RolloutMethod._unlink_all_validator = bv.Void()
RolloutMethod._unlink_most_inactive_validator = bv.Void()
RolloutMethod._add_member_to_exceptions_validator = bv.Void()
RolloutMethod._tagmap = {
    'unlink_all': RolloutMethod._unlink_all_validator,
    'unlink_most_inactive': RolloutMethod._unlink_most_inactive_validator,
    'add_member_to_exceptions': RolloutMethod._add_member_to_exceptions_validator,
}

RolloutMethod.unlink_all = RolloutMethod('unlink_all')
RolloutMethod.unlink_most_inactive = RolloutMethod('unlink_most_inactive')
RolloutMethod.add_member_to_exceptions = RolloutMethod('add_member_to_exceptions')

SharedFolderJoinPolicy._from_team_only_validator = bv.Void()
SharedFolderJoinPolicy._from_anyone_validator = bv.Void()
SharedFolderJoinPolicy._other_validator = bv.Void()
SharedFolderJoinPolicy._tagmap = {
    'from_team_only': SharedFolderJoinPolicy._from_team_only_validator,
    'from_anyone': SharedFolderJoinPolicy._from_anyone_validator,
    'other': SharedFolderJoinPolicy._other_validator,
}

SharedFolderJoinPolicy.from_team_only = SharedFolderJoinPolicy('from_team_only')
SharedFolderJoinPolicy.from_anyone = SharedFolderJoinPolicy('from_anyone')
SharedFolderJoinPolicy.other = SharedFolderJoinPolicy('other')

SharedFolderMemberPolicy._team_validator = bv.Void()
SharedFolderMemberPolicy._anyone_validator = bv.Void()
SharedFolderMemberPolicy._other_validator = bv.Void()
SharedFolderMemberPolicy._tagmap = {
    'team': SharedFolderMemberPolicy._team_validator,
    'anyone': SharedFolderMemberPolicy._anyone_validator,
    'other': SharedFolderMemberPolicy._other_validator,
}

SharedFolderMemberPolicy.team = SharedFolderMemberPolicy('team')
SharedFolderMemberPolicy.anyone = SharedFolderMemberPolicy('anyone')
SharedFolderMemberPolicy.other = SharedFolderMemberPolicy('other')

SharedLinkCreatePolicy._default_public_validator = bv.Void()
SharedLinkCreatePolicy._default_team_only_validator = bv.Void()
SharedLinkCreatePolicy._team_only_validator = bv.Void()
SharedLinkCreatePolicy._other_validator = bv.Void()
SharedLinkCreatePolicy._tagmap = {
    'default_public': SharedLinkCreatePolicy._default_public_validator,
    'default_team_only': SharedLinkCreatePolicy._default_team_only_validator,
    'team_only': SharedLinkCreatePolicy._team_only_validator,
    'other': SharedLinkCreatePolicy._other_validator,
}

SharedLinkCreatePolicy.default_public = SharedLinkCreatePolicy('default_public')
SharedLinkCreatePolicy.default_team_only = SharedLinkCreatePolicy('default_team_only')
SharedLinkCreatePolicy.team_only = SharedLinkCreatePolicy('team_only')
SharedLinkCreatePolicy.other = SharedLinkCreatePolicy('other')

SmartSyncPolicy._local_validator = bv.Void()
SmartSyncPolicy._on_demand_validator = bv.Void()
SmartSyncPolicy._other_validator = bv.Void()
SmartSyncPolicy._tagmap = {
    'local': SmartSyncPolicy._local_validator,
    'on_demand': SmartSyncPolicy._on_demand_validator,
    'other': SmartSyncPolicy._other_validator,
}

SmartSyncPolicy.local = SmartSyncPolicy('local')
SmartSyncPolicy.on_demand = SmartSyncPolicy('on_demand')
SmartSyncPolicy.other = SmartSyncPolicy('other')

SsoPolicy._disabled_validator = bv.Void()
SsoPolicy._optional_validator = bv.Void()
SsoPolicy._required_validator = bv.Void()
SsoPolicy._other_validator = bv.Void()
SsoPolicy._tagmap = {
    'disabled': SsoPolicy._disabled_validator,
    'optional': SsoPolicy._optional_validator,
    'required': SsoPolicy._required_validator,
    'other': SsoPolicy._other_validator,
}

SsoPolicy.disabled = SsoPolicy('disabled')
SsoPolicy.optional = SsoPolicy('optional')
SsoPolicy.required = SsoPolicy('required')
SsoPolicy.other = SsoPolicy('other')

TeamMemberPolicies._sharing_validator = TeamSharingPolicies_validator
TeamMemberPolicies._emm_state_validator = EmmState_validator
TeamMemberPolicies._office_addin_validator = OfficeAddInPolicy_validator
TeamMemberPolicies._all_field_names_ = set([
    'sharing',
    'emm_state',
    'office_addin',
])
TeamMemberPolicies._all_fields_ = [
    ('sharing', TeamMemberPolicies._sharing_validator),
    ('emm_state', TeamMemberPolicies._emm_state_validator),
    ('office_addin', TeamMemberPolicies._office_addin_validator),
]

TeamSharingPolicies._shared_folder_member_policy_validator = SharedFolderMemberPolicy_validator
TeamSharingPolicies._shared_folder_join_policy_validator = SharedFolderJoinPolicy_validator
TeamSharingPolicies._shared_link_create_policy_validator = SharedLinkCreatePolicy_validator
TeamSharingPolicies._all_field_names_ = set([
    'shared_folder_member_policy',
    'shared_folder_join_policy',
    'shared_link_create_policy',
])
TeamSharingPolicies._all_fields_ = [
    ('shared_folder_member_policy', TeamSharingPolicies._shared_folder_member_policy_validator),
    ('shared_folder_join_policy', TeamSharingPolicies._shared_folder_join_policy_validator),
    ('shared_link_create_policy', TeamSharingPolicies._shared_link_create_policy_validator),
]

TwoStepVerificationPolicy._require_tfa_enable_validator = bv.Void()
TwoStepVerificationPolicy._require_tfa_disable_validator = bv.Void()
TwoStepVerificationPolicy._other_validator = bv.Void()
TwoStepVerificationPolicy._tagmap = {
    'require_tfa_enable': TwoStepVerificationPolicy._require_tfa_enable_validator,
    'require_tfa_disable': TwoStepVerificationPolicy._require_tfa_disable_validator,
    'other': TwoStepVerificationPolicy._other_validator,
}

TwoStepVerificationPolicy.require_tfa_enable = TwoStepVerificationPolicy('require_tfa_enable')
TwoStepVerificationPolicy.require_tfa_disable = TwoStepVerificationPolicy('require_tfa_disable')
TwoStepVerificationPolicy.other = TwoStepVerificationPolicy('other')

ROUTES = {
}

