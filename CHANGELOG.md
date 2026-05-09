# Changelog

All notable changes to S40 Sign Tool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-05-10

### Added
- Git repository initialization
- `.gitignore` with comprehensive rules
- `.gitattributes` for proper line ending handling
- `LICENSE` file (MIT License)
- `CONTRIBUTING.md` with contribution guidelines
- `CHANGELOG.md` for version tracking

### Changed
- Improved `.gitignore` to cover more file types
- Better organization of ignored files

## [1.1.0] - 2026-05-09

### Added
- Multi-language support (Vietnamese and English)
- Language selector in GUI header
- Instant language switching (optimized from 2-3s to <0.1s)
- Language preference persistence via `config.json`

### Changed
- Optimized language switching mechanism
- Updated UI to use widget references instead of recreation
- Improved UX with no terminal flash during language change

### Performance
- 30x faster language switching

## [1.0.0] - 2026-05-09

### Added
- GUI application with Tkinter
- Certificate management (create, view, delete, export)
- JAR signing with automatic old signature removal
- All-in-one Windows script (`s40tool.bat`)
- Cross-platform shell scripts for Linux/Mac
- Standalone .exe build support with PyInstaller
- Interactive menu system
- Real-time logging in GUI
- JAD file auto-update after signing
- Certificate expiry checking
- Password change functionality

### Features
- **Sign JAR Tab**
  - Browse and select JAR files
  - Automatic old signature removal
  - JAD file auto-update option
  - Real-time signing progress
  - Signature verification

- **Manage Certificate Tab**
  - Create new certificates
  - View certificate information
  - Delete certificates
  - Export certificates to .cer format

- **Settings Tab**
  - Keystore configuration
  - Certificate details customization
  - About information

### Tools
- `s40_sign_app.py` - GUI application
- `sign_tool.py` - Command-line tool
- `s40tool.bat` - All-in-one Windows script
- `create_cert.sh` - Create certificate (Linux/Mac)
- `sign_jar.sh` - Sign JAR (Linux/Mac)
- `manage_cert.sh` - Manage certificate (Linux/Mac)
- `remove_signature.sh` - Remove signature (Linux/Mac)
- `run_app.sh` - Run GUI (Linux/Mac)

### Default Configuration
- Keystore: `certs/s40-keystore.jks`
- Alias: `s40cert`
- Password: `s40pass123`
- Validity: 3650 days (10 years)
- Algorithm: RSA 2048-bit

### Documentation
- Comprehensive README.md in Vietnamese
- Quick start guides
- Usage examples
- Troubleshooting section

## [Unreleased]

### Planned Features
- [ ] Support for multiple certificates
- [ ] Certificate import from external sources
- [ ] Batch signing for multiple JARs
- [ ] Custom signing profiles
- [ ] Certificate expiry notifications
- [ ] Dark mode theme
- [ ] More language support (Chinese, Japanese, etc.)
- [ ] Drag and drop JAR files
- [ ] Recent files history
- [ ] Signing statistics and logs

### Known Issues
- None reported yet

---

## Version History Summary

- **v1.1.1** (2026-05-10) - Git setup and documentation
- **v1.1.0** (2026-05-09) - Multi-language support
- **v1.0.0** (2026-05-09) - Initial release

## Links

- [GitHub Repository](#)
- [Issue Tracker](#)
- [Documentation](README.md)
- [Contributing Guidelines](CONTRIBUTING.md)

---

**Note:** This project follows [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backwards compatible manner
- PATCH version for backwards compatible bug fixes
